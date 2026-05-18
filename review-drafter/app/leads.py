"""Lead generation engine — find and convert practices, no Google API.

Two pure pieces, both usable today (the engine runs offline; the HIPAA
gate guarantees the sample is safe even with no API key):

  * qualify(): score a prospect from PUBLIC, non-clinical signals you
    can read off a Google listing by eye — no scraping creds needed.
  * free_sample(): turn a prospect's own public reviews into the
    cold-outreach weapon — real, HIPAA-safe replies in a near-voice,
    formatted to paste straight into an outreach email.

This is the top of the funnel and the pre-Google-API revenue path:
close on the sample, run the concierge trial (we deliver the approved
pack; the practice pastes — fully compliant, no automation), then
upgrade to the API pipeline once access lands.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from . import drafter
from .models import PracticeConfig, Review

HOT, WARM, COLD = "HOT", "WARM", "COLD"


@dataclass
class Prospect:
    practice_name: str
    review_count: int = 0
    avg_rating: float = 0.0
    unanswered_recent: int = 0      # recent reviews with no owner reply
    unanswered_negative: int = 0    # recent 1-2★ with no owner reply
    robotic_replies: bool = False   # existing replies look templated
    city: str = ""
    contact: str = ""


@dataclass
class LeadScore:
    score: int
    tier: str
    reasons: list[str] = field(default_factory=list)
    opener: str = ""


def qualify(p: Prospect) -> LeadScore:
    """Deterministic score 0-100. The pitch is in the data: public
    review pain = need + recurring value. Only public, non-clinical
    facts are ever used."""
    score = 0
    reasons: list[str] = []

    # Unanswered negatives = public reputational bleeding. Hottest.
    if p.unanswered_negative > 0:
        pts = min(45, 15 + p.unanswered_negative * 10)
        score += pts
        reasons.append(
            f"{p.unanswered_negative} recent 1–2★ with no owner reply "
            "(visible, fixable damage)")

    # Volume of unanswered recent reviews = ongoing, recurring pain.
    if p.unanswered_recent > 0:
        pts = min(30, p.unanswered_recent * 4)
        score += pts
        reasons.append(
            f"{p.unanswered_recent} recent reviews unanswered")

    # High review volume = the pain is continuous, not one-off.
    if p.review_count >= 50:
        score += 12
        reasons.append(
            f"{p.review_count} reviews — steady inflow, recurring value")
    elif p.review_count >= 20:
        score += 6

    # Low rating + unanswered = urgent; they're losing patients now.
    if p.avg_rating and p.avg_rating < 4.0 and p.unanswered_negative:
        score += 10
        reasons.append(
            f"{p.avg_rating:.1f}★ average while negatives sit unanswered")

    # They reply but badly = they care; easy to displace, warm not hot.
    if p.robotic_replies and p.unanswered_negative == 0:
        score += 8
        reasons.append("existing replies look templated/robotic")

    score = max(0, min(100, score))
    tier = HOT if score >= 55 else WARM if score >= 25 else COLD

    if p.unanswered_negative:
        opener = (f"I noticed {p.practice_name} has a couple of recent "
                  "1–2★ Google reviews without a reply yet — those are "
                  "the ones quietly costing you new patients.")
    elif p.unanswered_recent:
        opener = (f"I saw {p.practice_name} has several recent Google "
                  "reviews still waiting on a response.")
    elif p.robotic_replies:
        opener = (f"{p.practice_name}'s review replies look copy-pasted "
                  "— patients notice, and so does Google.")
    else:
        opener = (f"A quick note on {p.practice_name}'s Google reviews.")

    return LeadScore(score=score, tier=tier, reasons=reasons,
                     opener=opener)


def free_sample(reviews: list[Review], cfg: PracticeConfig,
                limit: int = 4) -> dict:
    """The cold-outreach deliverable: real, HIPAA-safe sample replies
    to the prospect's OWN public reviews. Lead with a negative if any
    (it's the most persuasive — that's the reply they're scared to
    write). Returns paste-ready markdown."""
    ordered = sorted(
        reviews, key=lambda r: (r.rating if r.rating is not None else 5))
    sample = ordered[:limit]
    drafted = drafter.draft_all(sample, cfg)

    lines = [f"# Sample replies for {cfg.practice_name}", "",
             "We wrote these for your *actual* recent Google reviews. "
             "Every one is checked against a HIPAA word-gate — no "
             "patient, treatment, or visit is ever confirmed. This is "
             "what we'd post for you (with your one-tap approval), in "
             "your voice, every week.", ""]
    all_passed = True
    for d in drafted:
        r = d.review
        rep = d.variants[0] if d.variants else None
        if d.used_fallback:
            all_passed = False
        lines += [
            f"### {r.rating or '—'}★ — {r.author or 'A patient'}",
            f"> {r.text}", "",
            f"**Our reply:** {rep.text if rep else ''}", "",
            f"_✓ {rep.why_safe if rep else ''}_", "",
            "---", ""]
    lines += [
        "We do this for every review, in your voice. You just tap "
        "approve (positives can be bundled). Reply to this email and "
        "we'll set up a free week on your real reviews."]
    return {
        "practice_name": cfg.practice_name,
        "count": len(sample),
        "all_passed": all_passed,
        "markdown": "\n".join(lines),
    }
