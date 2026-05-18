"""Parser: flexible CSV headers + plain-paste blocks. No API key."""
from app import parser
from app.config import FIXTURES_DIR


def test_csv_fixture_parses_all_rows():
    raw = (FIXTURES_DIR / "dental_reviews.csv").read_text()
    reviews = parser.parse(raw, is_csv=True)
    assert len(reviews) == 8
    assert reviews[0].rating == 5
    assert reviews[0].platform == "google"
    assert "Best dental office" in reviews[0].text


def test_csv_negative_flagging():
    raw = (FIXTURES_DIR / "dental_reviews.csv").read_text()
    reviews = parser.parse(raw, is_csv=True)
    negatives = [r for r in reviews if r.is_negative]
    assert len(negatives) == 3  # ratings 2, 1, 2


def test_csv_rejects_rows_without_text():
    raw = "author,rating,review\nBob,5,\nSue,4,Great place\n"
    reviews = parser.parse(raw, is_csv=True)
    assert len(reviews) == 1
    assert reviews[0].author == "Sue"


def test_paste_splits_on_dashes_and_blanklines():
    blocks = parser.parse("First review.\n---\nSecond review.", is_csv=False)
    assert len(blocks) == 2
    blanks = parser.parse("One.\n\nTwo.\n\nThree.", is_csv=False)
    assert len(blanks) == 3
    assert blanks[0].platform == "manual"


def test_rating_coercion_from_messy_values():
    raw = 'rating,review\n"4 stars",Decent\n"5/5",Great\n'
    reviews = parser.parse(raw, is_csv=True)
    assert [r.rating for r in reviews] == [4, 5]
