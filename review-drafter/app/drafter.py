"""Claude-API drafting with prompt caching + the compliance gate loop.

Flow per review: generate 2 variants -> compliance.scan each ->
regenerate with violations fed back (<= MAX retries) -> safe fallback.
No draft is returned until it passes the gate.

Runs WITHOUT an API key: returns safe fallback templates so the parser,
gate, and UI stay demoable offline.
"""
from __future__ import annotations

import json

from . import compliance, config, models, prompts
from .models import DraftedReview, DraftVariant, PracticeConfig, Review

_client = None


def _get_client():
    global _client
    if _client is None:
        import anthropic
        _client = anthropic.Anthropic(api_key=config.ANTHROPIC_API_KEY)
    return _client


def _call_model(user_prompt: str) -> list[dict]:
    """One model call. System block is cached (static), user is dynamic."""
    resp = _get_client().messages.create(
        model=config.ANTHROPIC_MODEL,
        max_tokens=config.MAX_OUTPUT_TOKENS,
        system=[{
            "type": "text",
            "text": prompts.STATIC_RULES,
            "cache_control": {"type": "ephemeral"},
        }],
        messages=[{"role": "user", "content": user_prompt}],
    )
    text = "".join(b.text for b in resp.content if b.type == "text")
    data = json.loads(text[text.index("{"): text.rindex("}") + 1])
    return data["variants"]


def _gate(variants: list[dict]) -> tuple[list[DraftVariant], list[str]]:
    """Keep only compliant variants; collect violations for regen."""
    safe: list[DraftVariant] = []
    all_violations: list[str] = []
    for v in variants:
        passed, violations = compliance.scan(v.get("text", ""))
        if passed:
            safe.append(DraftVariant(
                text=v["text"].strip(),
                why_safe=compliance.why_safe_note(v["text"]),
                label=v.get("label", ""),
            ))
        else:
            all_violations.extend(violations)
    return safe, all_violations


def draft_for_review(review: Review, practice: PracticeConfig) -> DraftedReview:
    fallback = [
        DraftVariant(text=fv["text"],
                     why_safe=compliance.why_safe_note(fv["text"]),
                     label=fv["label"])
        for fv in prompts.fallback_variants(
            review.is_negative, practice.office_phone, practice.sign_off)
    ]

    if not config.has_api_key():
        return DraftedReview(review=review, variants=fallback,
                             used_fallback=True)

    base_prompt = prompts.DRAFT_INSTRUCTIONS.format(
        practice_name=practice.practice_name,
        sign_off=practice.sign_off,
        office_phone=practice.office_phone or "(not set)",
        voice_json=json.dumps(practice.voice_profile),
        rating=review.rating if review.rating is not None else "unknown",
        platform=review.platform,
        review_text=review.text,
    )

    prompt = base_prompt
    for attempt in range(config.MAX_COMPLIANCE_RETRIES + 1):
        try:
            variants = _call_model(prompt)
        except Exception:
            break  # any API/parse failure -> safe fallback
        safe, violations = _gate(variants)
        if len(safe) >= 2:
            return DraftedReview(review=review, variants=safe[:2])
        if not violations:
            break
        prompt = base_prompt + prompts.REGEN_SUFFIX.format(
            violations="; ".join(sorted(set(violations))))

    return DraftedReview(review=review, variants=fallback,
                         used_fallback=True)


def draft_all(reviews: list[Review],
              practice: PracticeConfig) -> list[DraftedReview]:
    out = []
    for r in reviews:
        d = draft_for_review(r, practice)
        d.approval_mode = models.approval_mode(r, practice)
        out.append(d)
    return out
