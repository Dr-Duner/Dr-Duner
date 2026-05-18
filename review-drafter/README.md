# Review Response Drafter — Phase 1

First-draft MVP: paste/CSV dental reviews → 2 HIPAA-safe, voice-matched
draft replies each → edit → copy → mark posted → export approved CSV.

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
| The UI / approval flow | `app/templates/index.html`, `app/static/` |
| Routes / wiring | `app/main.py` |

## Boundaries (by design)

The compliance gate cannot be skipped. Nothing auto-posts — a human
approves and posts (v1). No PHI is persisted; CSV export is
user-initiated. See `service-operator` / `business-operations` skills
for what escalates to a human.
