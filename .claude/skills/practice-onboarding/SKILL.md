---
name: practice-onboarding
description: Use when adding a new dental practice to the Review Response Drafter — captures and stores the reusable per-practice config (voice profile, office phone, sign-off, do-not-say list) used by every later draft.
---

# Practice Onboarding

One-time per practice. Output is a reusable config the
`service-operator` and `review-reply-writing` skills consume.

## Two paths to the voice profile
- **Path A (preferred):** ask for 5–10 past replies they liked. Infer
  formality (1–5), warmth (1–5), sign-off, emoji use, typical length,
  recurring phrases. Confirm the inferred profile back to them.
- **Path B (no past replies):** 6-question brand-voice form:
  1. Formal or casual? (1–5)
  2. Warm/personal vs. brief/professional? (1–5)
  3. Sign-off line exactly as you want it (e.g. "— The Smile Dental Team")
  4. Emoji: none / sparing / yes
  5. Typical length: short (2 sent) / medium (3–4)
  6. Any phrase you ALWAYS use? Any you NEVER want used?

## Also capture (required)
- `office_phone` — used in the "please call us" line of negative-review
  replies. Without it, negative replies have no resolution channel.
- `practice_name` and `sign_off`.
- `never_say` list — practice-specific banned words/claims (on top of
  the HIPAA term list, which is non-negotiable and separate).
- Platforms in use (Google always; Yelp = manual paste only).

## Stored config shape (JSON, per practice)
```json
{
  "practice_name": "",
  "office_phone": "",
  "sign_off": "",
  "voice_profile": {
    "formality": 3, "warmth": 4, "emoji": "sparing",
    "length": "short", "always_say": [], "never_say": []
  },
  "platforms": ["google"]
}
```

## Rules
- Confirm the profile with the practice before first batch (they must
  recognize their own voice).
- HIPAA rules are global and NOT configurable here — `never_say` only
  *adds* restrictions, never relaxes compliance.
- Keep configs isolated per practice; never share across clients.
- Persist + commit the config so sessions/containers can resume.
