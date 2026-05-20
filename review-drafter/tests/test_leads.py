"""Lead qualifier scoring + free-sample weapon (offline)."""
from app.leads import HOT, COLD, Prospect, free_sample, qualify
from app.models import PracticeConfig, Review


def test_unanswered_negatives_make_it_hot():
    ls = qualify(Prospect("Acme Dental", review_count=120, avg_rating=3.6,
                           unanswered_recent=9, unanswered_negative=3))
    assert ls.tier == HOT
    assert ls.score >= 55
    assert any("1–2★" in r for r in ls.reasons)
    assert "Acme Dental" in ls.opener


def test_no_signal_is_cold():
    ls = qualify(Prospect("Quiet Dental"))
    assert ls.tier == COLD
    assert ls.score == 0


def test_score_is_clamped_0_100():
    ls = qualify(Prospect("Huge", review_count=999, avg_rating=2.0,
                           unanswered_recent=99, unanswered_negative=99))
    assert 0 <= ls.score <= 100


def test_opener_changes_with_signal():
    rob = qualify(Prospect("R", robotic_replies=True)).opener
    assert "copy-pasted" in rob


def test_free_sample_leads_with_negative_and_is_safe():
    cfg = PracticeConfig(practice_name="Bright Smile")
    reviews = [
        Review("Loved the staff!", author="Sam", rating=5),
        Review("Front desk was rude and I waited an hour",
               author="Pat", rating=1),
        Review("Decent visit overall", author="Lee", rating=3),
    ]
    out = free_sample(reviews, cfg, limit=3)
    assert out["count"] == 3
    assert "Bright Smile" in out["markdown"]
    # lowest rating first (the persuasive one)
    assert out["markdown"].index("1★") < out["markdown"].index("5★")
    assert isinstance(out["all_passed"], bool)


def test_free_sample_respects_limit():
    cfg = PracticeConfig(practice_name="P")
    reviews = [Review(f"r{i}", rating=5) for i in range(10)]
    assert free_sample(reviews, cfg, limit=2)["count"] == 2
