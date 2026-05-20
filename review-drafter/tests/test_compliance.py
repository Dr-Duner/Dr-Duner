"""Proves the HIPAA gate. Runs with no API key (deterministic)."""
from app import compliance

# Replies a compliant drafter should produce -> must PASS.
SAFE_REPLIES = [
    "Thank you so much for the kind words — it means a lot to our team.",
    "We're so sorry to hear this. Please call us at (555) 012-3456 so we "
    "can help make it right.",
    "This made our whole team smile. We're always here whenever you "
    "need us. — The Team",
    "We appreciate you taking the time to share your experience and "
    "we'd love the chance to talk it through with you directly.",
]

# Replies that confirm patient status / echo treatment -> must FAIL.
UNSAFE_REPLIES = [
    "So glad your root canal went smoothly — see you at your next cleaning!",
    "Thank you for choosing us for your filling, Jamie!",
    "We're glad we could fix your crown during your appointment.",
    "As our patient, your visit matters to us — your dentist will follow up.",
    "Sorry your extraction was painful, we'll do better next time you're in.",
]


def test_safe_replies_pass():
    for r in SAFE_REPLIES:
        passed, violations = compliance.scan(r)
        assert passed, f"should pass but flagged {violations}: {r!r}"


def test_unsafe_replies_fail():
    for r in UNSAFE_REPLIES:
        passed, violations = compliance.scan(r)
        assert not passed, f"should fail but passed: {r!r}"
        assert violations


def test_treatment_term_caught_even_if_reviewer_said_it():
    # We must not echo a procedure even when the reviewer disclosed it.
    passed, violations = compliance.scan(
        "We're so happy your implant turned out great!")
    assert not passed
    assert any("implant" in v for v in violations)


def test_why_safe_note_is_nonempty():
    assert compliance.why_safe_note("Thank you!").strip()
