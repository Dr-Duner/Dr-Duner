# Review Drafter — Phases 1 & 2

**We do all the labor; the client only approves.** Fully managed,
**Google-only**. The operator drafts + HIPAA-gates here (internal
console); the practice approves before anything posts, on their chosen
channel. Phase 1 (engine + console + gate + per-practice config) and
Phase 2 (approval state machine + persistence + 3-channel delivery +
working magic-link approval page + simulated Google post-back, tested
end-to-end offline) are built. Remaining is credential-gated only:
Google Business Profile API + per-practice OAuth, and real SMTP/Twilio
behind the `Sender` protocol — no design work left.

Flow: paste/CSV → 2 HIPAA-safe voice-matched drafts each → operator QA
→ "Send batch for client approval" (delivered on the practice's channel;
opted-in positives auto-approved) → route by rating (4–5★ bulk /
auto; 1–3★ + unrated always explicit) → client approves/edits/rejects
on the magic-link page (edits re-run the gate) → "Post approved"
(`SimulatedGoogleClient` until Google access is granted; a final HIPAA
scan is a hard pre-post backstop). State persists per practice under
`data/` (gitignored, isolated, public review text + decisions only — no
PHI).

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
HIPAA gate → operator QA → client approval → final pre-post HIPAA scan
→ post; client edits are re-gated before they can post. We do all the
labor; the client only approves. Google-only (Yelp has no reply API).
Persisted state is public review text + decisions only — no PHI,
gitignored, isolated per practice. See `service-operator` /
`business-operations` / `product-design` skills.
