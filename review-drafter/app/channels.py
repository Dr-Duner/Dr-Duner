"""Client approval delivery in all three channels.

The practice picks one at onboarding (email | link | sms). Rendering is
pure and tested here; *sending* is a pluggable Sender. The default
OutboxSender writes the exact message to data/<practice>/outbox/ so the
flow is provable offline. Real SMTP / Twilio are drop-in Senders behind
the same one-method protocol — no other code changes when access exists.

Positives (bulk/auto) get one grouped "approve all" action; negatives
and mixed (explicit) are listed individually with per-reply links. No
PHI: only the public review text + the gated reply ever appear.
"""
from __future__ import annotations

from typing import Protocol

from .models import PracticeConfig
from .store import ApprovalItem, _dir

# In production this is the public approval host; relative is fine for
# the offline harness and the magic-link page served by this app.
BASE_URL = ""


def _link(it: ApprovalItem, action: str) -> str:
    return f"{BASE_URL}/approve/{it.token}?item={it.id}&action={action}"


def _split(items: list[ApprovalItem]):
    pos = [i for i in items if i.approval_mode in ("bulk", "auto")]
    neg = [i for i in items if i.approval_mode == "explicit"]
    return pos, neg


def render_email_digest(cfg: PracticeConfig,
                        items: list[ApprovalItem]) -> dict:
    pos, neg = _split(items)
    page = items[0].token if items else ""
    subject = (f"{cfg.practice_name}: {len(items)} review repl"
               f"{'y' if len(items) == 1 else 'ies'} to approve")
    lines = [f"Hi — {len(items)} reply(ies) are ready. "
             "We wrote and HIPAA-checked them; just approve.", ""]
    if pos:
        lines.append(f"POSITIVE ({len(pos)}) — one click approves all:")
        lines.append(f"  Approve all positives: "
                      f"{BASE_URL}/approve/{page}?action=approve_all_positives")
        for i in pos:
            lines.append(f"  • {i.review.get('rating')}★ "
                         f"{i.review.get('author') or 'Anonymous'}: "
                         f"{i.reply[:80]}")
        lines.append("")
    for i in neg:
        lines.append(f"NEEDS YOUR OK — {i.review.get('rating')}★ "
                     f"{i.review.get('author') or 'Anonymous'}")
        lines.append(f"  Review: {i.review.get('text', '')[:160]}")
        lines.append(f"  Our reply: {i.reply}")
        lines.append(f"  Approve: {_link(i, 'approve')}")
        lines.append(f"  Reject:  {_link(i, 'reject')}")
        lines.append(f"  Edit:    {_link(i, 'edit')}")
        lines.append("")
    text = "\n".join(lines).rstrip() + "\n"
    return {"subject": subject, "text": text,
            "approve_page": f"{BASE_URL}/approve/{page}"}


def render_sms(cfg: PracticeConfig,
               items: list[ApprovalItem]) -> list[str]:
    pos, neg = _split(items)
    msgs: list[str] = []
    if pos:
        page = pos[0].token
        msgs.append(
            f"{cfg.practice_name}: {len(pos)} positive review repl"
            f"{'y' if len(pos) == 1 else 'ies'} ready. Reply OK to approve "
            f"all, or open {BASE_URL}/approve/{page}")
    for i in neg:
        msgs.append(
            f"{cfg.practice_name} {i.review.get('rating')}★ from "
            f"{i.review.get('author') or 'a patient'}. Proposed: "
            f"\"{i.reply[:90]}\" — reply YES to approve, NO to reject, "
            f"or EDIT for a link: {_link(i, 'edit')}")
    return msgs


def render_link_payload(cfg: PracticeConfig,
                        items: list[ApprovalItem]) -> dict:
    pos, neg = _split(items)
    return {
        "practice_name": cfg.practice_name,
        "positives": [_card(i) for i in pos],
        "explicit": [_card(i) for i in neg],
    }


def _card(i: ApprovalItem) -> dict:
    return {
        "id": i.id, "token": i.token, "status": i.status,
        "rating": i.review.get("rating"),
        "author": i.review.get("author") or "Anonymous",
        "review": i.review.get("text", ""),
        "reply": i.reply, "why_safe": i.why_safe,
        "mode": i.approval_mode,
    }


class Sender(Protocol):
    def send(self, cfg: PracticeConfig,
             items: list[ApprovalItem]) -> dict: ...


class OutboxSender:
    """Offline default: writes the rendered message to a file. Proves
    delivery content without an email/SMS provider."""

    live = False

    def send(self, cfg: PracticeConfig,
             items: list[ApprovalItem]) -> dict:
        if not items:
            return {"sent": 0, "channel": cfg.approval_channel}
        out = _dir(items[0].practice) / "outbox"
        out.mkdir(parents=True, exist_ok=True)
        ch = cfg.approval_channel
        if ch == "sms":
            msgs = render_sms(cfg, items)
            (out / "sms.txt").write_text("\n---\n".join(msgs))
            payload = {"messages": msgs}
        elif ch == "link":
            import json
            payload = render_link_payload(cfg, items)
            (out / "link.json").write_text(json.dumps(payload, indent=2))
        else:  # email (default)
            d = render_email_digest(cfg, items)
            (out / "email.txt").write_text(
                f"Subject: {d['subject']}\n\n{d['text']}")
            payload = d
        return {"sent": len(items), "channel": ch, "to": cfg.approver_contact,
                "preview": payload}


def get_sender(cfg: PracticeConfig) -> Sender:
    # Real SMTP/Twilio senders slot in here keyed on cfg.approval_channel
    # once provider credentials exist. Default stays offline-provable.
    return OutboxSender()
