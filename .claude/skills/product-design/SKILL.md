---
name: product-design
description: Use when designing the Review Response Drafter's product and UX — the internal operator console for reviewing/posting gated drafts, the practice onboarding flow, and the sales demo. The client is never a UI user; the operator is.
---

# Product Design

This is a **fully managed service**, not self-serve software. The UI is
an **internal operator console** — the operator (us) is the only user.
The dental practice never logs in, never approves, never posts; they
granted Google access once and otherwise do nothing. Design the console
for operator *throughput*, and design the client *experience* as
"reviews just get handled." This skill specifies the UI; the Phase-1
console is built (see `review-drafter/SPEC.md`).

## Design principles
- The console optimizes **operator throughput**: many practices' gated
  drafts reviewed and posted fast, with confidence.
- Trust/speed for the operator: show *why each draft is HIPAA-safe*
  inline so a post decision takes seconds.
- The operator reviews & posts. Never the client. Never fully
  autonomous (v1/v2). Posting to a practice's public listing is
  high-consequence — the console must make the gate + the post action
  unmissable and deliberate.
- Client-facing "design" = zero surface area: a clean weekly recap
  (proof of work), and a smooth one-time onboarding. Nothing else.

## Operator console spec (Phase 1, single page)
1. **Intake bar:** paste-reviews textarea OR "Upload CSV"; confirm
   "Found N reviews" before drafting. (Phase 2: auto-fed by Google API
   per practice — operator picks a practice queue instead of pasting.)
2. **Review card:** reviewer name, stars, platform, date, review text;
   practice context visible.
3. **Two gated draft variants** (A short/warm, B fuller), each with:
   - inline editable text box
   - green "Why this is safe" one-liner (`hipaa-review-compliance`)
   - **Copy** button
   - **Confirm & post** (Phase 1: marks posted / Phase 2: posts to
     Google via API) / **Skip**
4. **Status chips:** drafted / gated / posted / skipped.
5. **Export CSV** of what was posted (operator record).

Non-negotiable rules:
- No draft shown until it passes the compliance gate.
- The post action is explicit and deliberate — never a default, never
  bulk-auto. Negative reviews visually flagged, handled first.
- Editing never loses the original. No PHI persisted in Phase 1.

## Onboarding flow (one-time, per practice — minimal client effort)
Drive `practice-onboarding`: capture voice (paste past replies OR the
6-Q form), office phone, sign-off, AND the Google OAuth grant +
written authorization to post on their behalf. Confirm the voice back
once ("Does this sound like you?"). After this, the client is done.

## The demo (sales asset)
30-sec: a nasty 1★ review → safe warm draft with the why-safe note →
posted. Framing to the prospect: "this happens for every review,
automatically — you do nothing." (`sales-closing` uses it.)

## Anti-goals
No client-facing app. No client approval UX. No vanity dashboards, no
autonomous bulk-posting, no AI jargon. The client's "product" is the
absence of work + a weekly proof-of-work recap.
