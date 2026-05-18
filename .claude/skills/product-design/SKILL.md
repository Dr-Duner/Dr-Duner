---
name: product-design
description: Use when designing the Review Response Drafter's product and UX — especially the review-handling interface (the approval queue), the onboarding flow, and the demo. Encodes the UI spec and design principles for non-technical dental office staff.
---

# Product Design

The user is a non-technical dental office manager who is busy and a
little scared of doing reviews wrong. Design for relief and trust, not
features. Note: this skill *specifies* the UI; the UI itself is a
Phase-1 build deliverable (see `review-drafter/SPEC.md`).

## Design principles
- 30 seconds per review or we failed. Every screen optimizes time-to-
  approve.
- Trust is the feature: show *why each draft is HIPAA-safe* inline.
- Zero learning curve: one screen, no manual, no jargon, no settings
  maze. An office manager should get it without a call.
- The human approves & posts (v1). Never auto-post. Make the human
  feel in control, not automated over.

## The review-handling UI spec (Phase 1, single page)
Layout — one queue, one review at a time or a simple list:
1. **Intake bar (top):** paste-reviews textarea OR "Upload CSV". After
   submit, confirm "Found N reviews" before drafting.
2. **Review card:** reviewer name, stars, platform, date, review text.
3. **Two draft variants** (A short/warm, B fuller), each with:
   - inline editable text box
   - a green "Why this is safe" one-liner (from
     `hipaa-review-compliance`)
   - **Copy** button (copies final text to clipboard)
   - **Mark posted** / **Skip** buttons
4. **Status chips:** drafted / approved / posted / skipped, per review.
5. **Export approved CSV** button.
6. Empty/zero state: friendly "Paste your reviews to get started."

Non-negotiable UX rules:
- No draft is ever shown until it passes the compliance gate.
- Negative reviews visually flagged (needs attention first).
- Nothing destructive without undo; editing never loses the original.
- No PHI persisted; CSV export is user-initiated, local.

## Onboarding flow (first run, per practice)
Drive `practice-onboarding`: 6-question voice form OR "paste 5–10 past
replies", capture office phone + sign-off, confirm the inferred voice
back ("Does this sound like you?"), then straight into the queue.

## The demo (sales asset)
A 30-sec scripted path: paste one nasty 1★ review → safe warm draft
appears with the why-safe note → edit a word → Copy → done. This IS
the pitch (`sales-closing` uses it).

## Anti-goals
No dashboards of vanity charts in v1, no multi-step wizards, no
account/settings sprawl, no AI jargon in the UI. Boring and fast wins.
