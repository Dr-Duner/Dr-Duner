"""Phase 2: approval state machine, channels, simulated Google post."""
import pytest

from app import approvals, channels, google_gbp, store
from app.models import DraftedReview, DraftVariant, PracticeConfig, Review


@pytest.fixture(autouse=True)
def tmp_data(tmp_path, monkeypatch):
    monkeypatch.setattr(store, "DATA_DIR", tmp_path / "data")


def _drafted(rating, reply, mode):
    r = Review(text=f"review {rating}", author=f"A{rating}", rating=rating)
    return DraftedReview(review=r, approval_mode=mode,
                         variants=[DraftVariant(text=reply,
                                                why_safe="generic thanks")])


POS = PracticeConfig(auto_approve_positives=False, approval_channel="email")
AUTO = PracticeConfig(auto_approve_positives=True, approval_channel="sms")


def test_explicit_pending_auto_approved_immediately():
    items = approvals.create_from_drafted("p1", AUTO, [
        _drafted(5, "Thanks so much!", "auto"),
        _drafted(1, "Sorry to hear that, please call us.", "explicit"),
    ])
    by_mode = {i.approval_mode: i for i in items}
    assert by_mode["auto"].status == store.APPROVED
    assert by_mode["explicit"].status == store.PENDING


def test_bulk_approve_skips_explicit():
    approvals.create_from_drafted("p2", POS, [
        _drafted(5, "Thank you!", "bulk"),
        _drafted(4, "We appreciate it!", "bulk"),
        _drafted(2, "Please call our office.", "explicit"),
    ])
    res = approvals.bulk_approve_positives("p2")
    assert res["approved"] == 2
    explicit = [i for i in store.list_items("p2")
                if i.approval_mode == "explicit"][0]
    assert explicit.status == store.PENDING


def test_token_action_approve_and_reject():
    items = approvals.create_from_drafted("p3", POS, [
        _drafted(1, "We're sorry, please call us.", "explicit"),
        _drafted(2, "Please reach out to our office.", "explicit"),
    ])
    a, b = items
    assert approvals.apply_action(a.token, "approve", a.id)["ok"]
    assert store.get("p3", a.id).status == store.APPROVED
    assert approvals.apply_action(b.token, "reject", b.id)["ok"]
    assert store.get("p3", b.id).status == store.REJECTED


def test_edit_failing_hipaa_is_refused_and_not_posted():
    items = approvals.create_from_drafted("p4", POS, [
        _drafted(1, "We're sorry, please call us.", "explicit")])
    it = items[0]
    bad = approvals.apply_action(
        it.token, "approve", it.id,
        edited_text="Thanks for trusting us with your root canal!")
    assert bad["ok"] is False
    assert bad["violations"]
    fresh = store.get("p4", it.id)
    assert fresh.status == store.PENDING
    assert "root canal" not in fresh.reply


def test_edit_passing_hipaa_updates_reply():
    items = approvals.create_from_drafted("p5", POS, [
        _drafted(1, "Old reply, please call us.", "explicit")])
    it = items[0]
    ok = approvals.apply_action(
        it.token, "approve", it.id,
        edited_text="We're grateful for your feedback and are here to help.")
    assert ok["ok"]
    assert "grateful" in store.get("p5", it.id).reply


def test_simulated_post_transitions_to_posted():
    approvals.create_from_drafted("p6", AUTO, [
        _drafted(5, "Thank you so much!", "auto")])
    res = approvals.post_approved("p6", google_gbp.SimulatedGoogleClient())
    assert res["posted"] == 1 and res["live"] is False
    assert store.list_items("p6")[0].status == store.POSTED


def test_live_google_refuses_without_credentials():
    with pytest.raises(google_gbp.GoogleNotConfigured):
        google_gbp.LiveGoogleClient().post_reply("p", "ref", "hi")


def test_email_digest_groups_and_links():
    items = approvals.create_from_drafted("p7", POS, [
        _drafted(5, "Thanks!", "bulk"),
        _drafted(1, "Please call us.", "explicit")])
    d = channels.render_email_digest(POS, items)
    assert "approve_all_positives" in d["text"]
    assert "/approve/" in d["text"]
    assert "NEEDS YOUR OK" in d["text"]


def test_sms_render_one_per_negative():
    items = approvals.create_from_drafted("p8", AUTO, [
        _drafted(5, "Thanks!", "auto"),
        _drafted(1, "Please call us.", "explicit"),
        _drafted(2, "Please call us.", "explicit")])
    msgs = channels.render_sms(AUTO, items)
    # one positives summary + one per explicit
    assert len(msgs) == 3
    assert any("reply YES to approve" in m for m in msgs)


def test_decided_item_not_resurrected_on_redraft():
    d = [_drafted(1, "Please call us.", "explicit")]
    items = approvals.create_from_drafted("p9", POS, d)
    approvals.apply_action(items[0].token, "approve", items[0].id)
    again = approvals.create_from_drafted("p9", POS, d)
    assert again[0].status == store.APPROVED  # unchanged, not back to pending
