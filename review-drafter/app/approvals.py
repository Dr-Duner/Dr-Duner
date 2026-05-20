"""Approval state machine — the Phase 2 consent boundary.

Nothing reaches Google without the practice's approval. 1-3★ and
unrated are always explicit. 4-5★ are bulk-approvable, or auto if the
practice opted in (then they enter the queue already approved). Any
client edit is re-run through the HIPAA gate before it can post — an
edit that introduces a violation is refused, never posted.
"""
from __future__ import annotations

from . import compliance, store
from .google_gbp import GoogleClient, get_client
from .models import DraftedReview, PracticeConfig


def create_from_drafted(
    practice: str, cfg: PracticeConfig, drafted: list[DraftedReview]
) -> list[store.ApprovalItem]:
    items: list[store.ApprovalItem] = []
    for d in drafted:
        r = d.review
        chosen = d.variants[0] if d.variants else None
        iid = store.item_id(practice, r.author, r.date, r.text)
        existing = store.get(practice, iid)
        if existing and existing.status != store.PENDING:
            items.append(existing)  # decided already; don't disturb
            continue
        it = store.ApprovalItem(
            id=iid,
            practice=practice,
            review=r.to_dict(),
            reply=chosen.text if chosen else "",
            why_safe=chosen.why_safe if chosen else "",
            approval_mode=d.approval_mode,
            token=(existing.token if existing else store.new_token()),
            channel=cfg.approval_channel,
        )
        if d.approval_mode == "auto":
            it.status = store.APPROVED
            it.decided_at = store._now()
            it.log("auto_approved", reason="practice opted in (4-5★)")
        else:
            it.log("queued", mode=d.approval_mode)
        items.append(it)
    return store.upsert_batch(practice, items)


def _apply_text(it: store.ApprovalItem, text: str) -> tuple[bool, list[str]]:
    """Re-gate edited text. Returns (ok, violations)."""
    passed, violations = compliance.scan(text)
    if passed:
        it.reply = text
        it.why_safe = compliance.why_safe_note(text)
    return passed, violations


def apply_action(
    token: str, action: str, item_id: str | None = None,
    edited_text: str | None = None,
) -> dict:
    found = store.find_by_token(token)
    if not found:
        return {"ok": False, "error": "invalid or expired link"}
    practice, _ = found
    target_id = item_id or found[1].id
    it = store.get(practice, target_id)
    if it is None:
        return {"ok": False, "error": "item not found"}
    if it.status in (store.POSTED, store.REJECTED):
        return {"ok": False, "error": f"already {it.status}"}

    if action == "reject":
        it.status = store.REJECTED
        it.decided_at = store._now()
        it.log("rejected", by="client")
        store.save(it)
        return {"ok": True, "status": it.status}

    if action in ("approve", "edit"):
        if edited_text is not None and edited_text.strip():
            ok, violations = _apply_text(it, edited_text.strip())
            if not ok:
                it.log("edit_refused", violations=violations)
                store.save(it)
                return {"ok": False, "error": "edit failed HIPAA gate",
                        "violations": violations}
        if action == "edit":
            it.log("edited", by="client")
            store.save(it)
            return {"ok": True, "status": it.status, "reply": it.reply}
        it.status = store.APPROVED
        it.decided_at = store._now()
        it.log("approved", by="client")
        store.save(it)
        return {"ok": True, "status": it.status}

    return {"ok": False, "error": f"unknown action '{action}'"}


def bulk_approve_positives(practice: str) -> dict:
    """One-click: approve all pending bulk/auto (4-5★) items. Never
    touches explicit (1-3★) items."""
    n = 0
    for it in store.list_items(practice, store.PENDING):
        if it.approval_mode in ("bulk", "auto"):
            it.status = store.APPROVED
            it.decided_at = store._now()
            it.log("approved", by="client", via="bulk_positives")
            store.save(it)
            n += 1
    return {"ok": True, "approved": n}


def post_approved(practice: str, client: GoogleClient | None = None) -> dict:
    """Push every approved-but-unposted reply to Google (simulated by
    default). A final HIPAA scan is a hard pre-post backstop."""
    client = client or get_client()
    posted, blocked = 0, []
    for it in store.list_items(practice, store.APPROVED):
        ok, violations = compliance.scan(it.reply)
        if not ok:
            it.log("post_blocked", violations=violations)
            store.save(it)
            blocked.append({"id": it.id, "violations": violations})
            continue
        ref = client.post_reply(
            practice, it.review.get("author", "") or it.id, it.reply)
        it.status = store.POSTED
        it.posted_at = store._now()
        it.posted_ref = ref
        it.log("posted", ref=ref, live=getattr(client, "live", False))
        store.save(it)
        posted += 1
    return {"ok": True, "posted": posted, "blocked": blocked,
            "live": getattr(client, "live", False)}
