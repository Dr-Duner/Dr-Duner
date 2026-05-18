---
name: service-operator
description: Use to run the Review Response Drafter service end-to-end for one or more practices — the master runbook that orchestrates onboarding, review intake, drafting, the compliance gate, the approval queue, and the weekly recap. Invoke this to "run the business" autonomously.
---

# Service Operator (master runbook)

The orchestration brain. This skill sequences the others. Run it to
operate the service for a practice without step-by-step prompting.

## Skill order of operations
1. `practice-onboarding` → produces/loads the practice config
   (voice_profile, office_phone, sign_off, never-say list).
2. Intake: ingest pasted text or CSV → normalized `Review[]`
   (author, rating, text, platform, date). Treat all input as
   sensitive: no logging of review bodies, no third-party analytics.
3. For each review: `review-reply-writing` → 2 draft variants.
4. `hipaa-review-compliance` → gate. FAIL → regen (max 2) → safe
   fallback. Nothing reaches a human un-gated. Attach "why safe" note.
5. Deliver to the approval queue (single page: review → 2 drafts →
   edit → Copy → Mark posted → export approved CSV). NEVER auto-post
   in v1; human approves and posts.
6. Track status per review: drafted / approved / posted / skipped.
7. Weekly recap per practice (see below).

## CSV intake contract
Accept flexible headers; map to: author, rating(1–5), text, platform
(google/yelp/other), date. Tolerate missing date/author. Reject rows
with empty text. Confirm row count back to the user before drafting.

## Weekly recap (per practice)
Short, plain message: # reviews handled, avg rating this week, # still
needing approval, any 1–2★ that need fast attention, rating trend vs.
last week. No PHI. This is the retention touchpoint — keep it human.

## Operating rules
- The compliance gate is absolute and cannot be skipped for speed.
- Human-in-the-loop always in v1: we draft, they approve & post.
  Document this; it's the liability posture.
- Yelp is manual-paste only (API/scrape constraints — see
  `google-reviews-expert`).
- One practice's config/data never bleeds into another's.
- At every stopping point: commit + push (container is ephemeral).
- Escalate to the human operator (not silently guess) when: a review
  contains a threat/legal/medical-emergency claim, a draft can't pass
  compliance after retries on a sensitive review, or a practice asks
  for something outside this runbook.

## State of the build
Phase 1 = manual paste/CSV + queue (current). Phase 2 = Google API
auto-ingest + email digest. See `review-drafter/SPEC.md` for the
roadmap; that spec + this runbook are the source of truth.
