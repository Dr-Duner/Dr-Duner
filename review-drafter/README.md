# Review Drafter — Phase 1 (Operator Console)

**Internal operator tool, not a client product.** This is a fully
managed, operator-in-the-loop, **Google-only** service: the practice
does nothing; the operator (us) reviews HIPAA-gated drafts here and
posts them. Phase 1 = the drafting/compliance engine + operator console
fed by manual paste/CSV (the testing/ops harness that proves the
engine). Phase 2 (required for the promise) = Google Business Profile
API auto-ingest + operator-gated post-back. There is intentionally no
client-facing app.

Flow: paste/CSV reviews → 2 HIPAA-safe, voice-matched drafts each →
operator QA → route by rating (4–5★ bulk-approvable / auto if the
practice opted in; 1–3★ explicit client approval) → client approves on
their channel (email | magic-link | SMS) → we post. Phase 1 simulates
the approve/post step (mark posted + CSV record); Phase 2 wires the
real channels + Google API.

Spec: `SPEC.md`. Business logic skills: `../.claude/skills/`.

## Run

```bash
cd review-drafter
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # optional: add ANTHROPIC_API_KEY
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000. **No API key needed to try it** — without
one, the parser and HIPAA gate are fully live and drafts use the safe
fallback templates. Add `ANTHROPIC_API_KEY` to `.env` for real
voice-matched drafting.

Quick demo: pick a practice, paste a review (or upload
`fixtures/dental_reviews.csv`), click **Draft replies**.

## Test (no API key required)

```bash
pytest -q
```

`tests/test_compliance.py` is the guardrail proof — it asserts the
deterministic HIPAA gate passes safe replies and fails any that confirm
a patient or echo a treatment, even when the reviewer mentioned it.

## Where to change things (first-draft, built to edit)

| Want to change… | Edit |
|---|---|
| HIPAA banned terms / rules | `app/compliance.py` (term lists at top) |
| Model prompt, few-shots, fallbacks | `app/prompts.py` |
| Model / API key / retry knobs | `.env` and `app/config.py` |
| A practice's voice/phone/sign-off | `practices/<name>.json` |
| Input formats accepted | `app/parser.py` |
| Operator console UI | `app/templates/index.html`, `app/static/` |
| Routes / wiring | `app/main.py` |

## Boundaries (by design)

The compliance gate cannot be skipped. Nothing posts to a practice's
public listing without that practice's approval — explicit per-reply
for 1–3★, bulk (or opt-in auto) for 4–5★. Client approval is the
liability anchor (consent to what posts in their name). Layered safety:
HIPAA gate → operator QA → client approval → post. We do all the labor;
the client only approves. Google-only (Yelp has no reply API). No PHI
persisted in Phase 1. See `service-operator` / `business-operations` /
`product-design` skills.
