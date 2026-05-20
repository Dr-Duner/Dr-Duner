"""Approval routing: positives bulk/auto, negatives+mixed explicit."""
from app.models import PracticeConfig, Review, approval_mode

DEFAULT = PracticeConfig()
AUTO = PracticeConfig(auto_approve_positives=True)


def test_negative_always_explicit():
    for stars in (1, 2):
        r = Review(text="bad", rating=stars)
        assert approval_mode(r, DEFAULT) == "explicit"
        assert approval_mode(r, AUTO) == "explicit"  # never auto a 1-2★


def test_mixed_three_star_is_explicit():
    r = Review(text="meh", rating=3)
    assert approval_mode(r, DEFAULT) == "explicit"
    assert approval_mode(r, AUTO) == "explicit"


def test_unknown_rating_is_explicit():
    r = Review(text="pasted, no rating", rating=None)
    assert approval_mode(r, DEFAULT) == "explicit"


def test_positive_is_bulk_by_default():
    for stars in (4, 5):
        assert approval_mode(Review(text="great", rating=stars),
                             DEFAULT) == "bulk"


def test_positive_is_auto_when_practice_opted_in():
    for stars in (4, 5):
        assert approval_mode(Review(text="great", rating=stars),
                             AUTO) == "auto"


def test_config_roundtrip_defaults():
    c = PracticeConfig.from_dict({})
    assert c.approval_channel == "email"
    assert c.auto_approve_positives is False
