---
name: review-reply-writing
description: Use when drafting the actual reply text to a customer/patient review and matching a specific business's voice. The creative-writing craft layer — produces approve-on-first-read replies. Always run hipaa-review-compliance after this for healthcare clients.
---

# Review Reply Writing

Goal: a reply the owner approves without rewriting. Quality here is the
retention driver. Pair with `hipaa-review-compliance` (it has veto).

## Voice profile (per practice, reused every draft)
Capture/store as JSON: formality (formal↔casual 1–5), warmth (1–5),
uses reviewer first name? (for non-healthcare only), sign-off line,
emoji (none/sparing/yes), typical length (short/medium), always-say
phrases, never-say phrases. If no past replies exist, the
`practice-onboarding` skill collects this via questionnaire.

## Per-rating playbook
- **5★:** short, specific-but-generic gratitude; mirror one *non-PHI*
  theme they raised (friendliness, comfort, front desk); end on warmth.
  Don't gush; 2–3 sentences.
- **4★:** thank + light "we'd love to make it a 5-star experience"
  without fishing; invite back generally.
- **3★:** acknowledge the mixed experience honestly; no defensiveness;
  offer a private channel for the negative part.
- **1–2★:** lead with empathy, never defensiveness, never "but";
  validate the feeling, take it offline fast; one calm, human
  paragraph. De-escalation > winning.

## De-escalation language
Use: "I'm sorry to hear", "we take this seriously", "we'd like to make
this right", "please reach out so we can help."
Avoid: "Actually", "Our records show", "As you know", "However",
"We disagree", anything that confirms a visit or argues facts.

## Style rules
- Sound like a person at the practice, not a brand bot. Vary openings
  across drafts (don't start every reply "Thank you for…").
- Match the voice profile's length/formality/emoji exactly.
- One clear ask max (call us / come back), never multiple CTAs.
- No marketing slogans, no SEO keyword stuffing, no signature spam.
- Always produce **2 variants**: (A) short & warm, (B) slightly fuller.

## Output
2 variants + the chosen sign-off applied. Hand off to
`hipaa-review-compliance` before anything is shown.
