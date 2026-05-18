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
5. Deliver gated drafts to the **operator console** (internal, never
   client-facing). The OPERATOR — us, running this business, never the
   client — reviews and posts. Phase 1: operator marks posted (paste/CSV
   harness). Phase 2: operator clicks → Google Business Profile API
   posts to the practice's listing. Never autonomous; never the client.
6. Track status per review: drafted / gated / posted / skipped.
7. Weekly recap to the practice (see below) — proof of work, not a
   to-do for them.

## The model (do not regress)
Fully managed, operator-in-the-loop, **Google-only**. The client does
nothing: no client login, no client approval, no client posting. They
grant Google access once at onboarding; we run it. The human safety net
is at OUR cost (operator review), never client effort.

## CSV intake contract
Accept flexible headers; map to: author, rating(1–5), text, platform
(google/other), date. Tolerate missing date/author. Reject rows with
empty text. Confirm row count before drafting.

## Weekly recap (per practice)
Short, plain message: # reviews handled & posted, avg rating this week,
any 1–2★ we fast-tracked, rating trend vs. last week. No PHI. This is
proof we're earning the fee — the retention touchpoint.

## Operating rules
- The compliance gate is absolute and cannot be skipped for speed.
- Posting is operator-owned and operator-gated. Never the client, never
  fully autonomous (v1/v2). We post to the practice's public listing —
  they are publicly liable for what lands there; gate + operator review
  are the safety net. Document this; it's the liability posture.
- Yelp is excluded — no reply API. Google-only; never imply Yelp.
- One practice's config/data never bleeds into another's.
- At every stopping point: commit + push (container is ephemeral).
- Escalate to the human operator (not silently guess) when: a review
  contains a threat/legal/medical-emergency claim, a draft can't pass
  compliance after retries on a sensitive review, or a practice asks
  for something outside this runbook.

## State of the build
Phase 1 = engine + operator console + HIPAA gate, fed by manual
paste/CSV (built; the ops/testing harness, NOT the client product).
Phase 2 (required for the promise) = Google Business Profile API:
auto-ingest + operator-gated post-back. See `review-drafter/SPEC.md`;
that spec + this runbook are the source of truth.
