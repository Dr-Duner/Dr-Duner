---
name: sales-closing
description: Use to convert engaged/demo'd dental leads into paying customers — the discovery-to-close motion, the free-batch demo, pricing conversation, trial setup, objection handling at the close, and the handoff to onboarding.
---

# Sales Closing

Turn interest into a paying practice. The product demos itself — let it
do the selling; you remove friction. Outreach/objections at first
touch live in `cold-outreach-dental`; this is the close.

## The motion (free batch → trial → paid)
1. **Deliver the free batch fast.** Their last ~10 real reviews, drafted
   in their voice, HIPAA-gated, each with a "why this is safe" note.
   This is the entire pitch. Speed > polish.
2. **Walk it (5 min).** Show their real review → safe, on-voice reply →
   why-safe note. Then the key line: "Grant us Google access once —
   after that every review is answered for you, HIPAA-safe. You never
   touch it." Sell the absence of work.
3. **Quantify their pain back.** "You said reviews take ~4–5 hrs/week
   and you worry about saying the wrong thing. That goes to zero —
   we handle all of it, HIPAA-checked, you do nothing."
4. **Price simply, once, then stop talking.** One monthly number by
   their review volume. Don't over-explain or discount reflexively.
5. **Lower the risk:** "Free for the first week on your real reviews —
   if it's not worth it, walk away."
6. **Get the onboarding slot** (the one-time Google grant + voice
   capture), not "think about it." That 15-min onboarding is the only
   thing they ever have to do.

## Close-stage objections
- "Need to think about it." → "Totally — start the free week while you
  think; nothing to lose." (Convert thinking into trialing.)
- "Have to ask the dentist/owner." → offer a 1-paragraph forward-able
  ROI + compliance note (from `dental-practice-marketing`).
- "Is it actually HIPAA-safe?" → the compliance one-pager + "your
  counsel can review our rules." Strength, not weakness.
- "Price." → reframe vs. staff hours saved + cost of one HIPAA misstep;
  hold the price, offer the trial instead of a discount.
- "We'll just keep doing it ourselves." → "That's exactly what you stop
  doing — we handle every review for you, HIPAA-safe, in your voice.
  Free week to prove it?"
- "Can we approve replies first?" → "We keep a human (us) reviewing
  every reply before it posts — that's included. You don't have to be
  in the loop, but your voice and our HIPAA gate always are."

## Rules
- Sell relief and safety, not "AI." Never oversell ROI or invent
  metrics — credibility is the asset here.
- One clear ask per conversation. Always end with a scheduled next step.
- Won → immediately trigger `practice-onboarding`, then
  `service-operator`. Update `lead-pipeline` the same touch.
- Don't chase past the cadence in `lead-pipeline`; a graceful "door
  open" beats a pushy loss in a referral-driven niche.
