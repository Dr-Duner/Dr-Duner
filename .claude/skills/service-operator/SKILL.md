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
5. Gated drafts → **operator console** (internal QA, never client-
   facing). Operator spot-checks.
6. **Route by rating:** 4–5★ → bulk-approvable (or auto-approve if the
   practice opted in via `auto_approve_positives`). 1–3★ → ALWAYS
   explicit per-reply client approval. Never auto-post a 1–3★.
7. **Send for client approval** on the practice's chosen channel
   (`approval_channel`: email digest | magic-link page | SMS) to their
   `approver_contact`. Client can approve / edit / reject.
8. **On approval → post.** Phase 1: operator marks posted (paste/CSV
   harness). Phase 2: approval triggers Google Business Profile API
   post to the practice's listing. Rejected → drop. Edited → post the
   client's edited text (re-run the gate on it first).
9. Track status per review: drafted / gated / awaiting-approval /
   approved / posted / rejected.
10. Weekly recap to the practice — proof of work, not a to-do.

## The model (do not regress)
Fully managed, **client-approves-then-we-post**, **Google-only**. We do
100% of the labor (ingest, draft, gate, send, post). The client's only
action is a fast approve/edit/reject — explicitly for 1–3★, bulk or
opt-in-auto for 4–5★. That approval is the liability anchor (they
consent to what posts in their name); never remove it without an
explicit per-practice auto-approve opt-in. Never a client authoring app.

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
- Nothing posts to a practice's public listing without that practice's
  approval (explicit for 1–3★; bulk/opt-in-auto for 4–5★). Client
  approval is the liability anchor — they consent to what posts in
  their name. Layered safety: HIPAA gate → operator QA → client
  approval → post. Re-run the gate on any client-edited text.
- Yelp is excluded — no reply API. Google-only; never imply Yelp.
- One practice's config/data never bleeds into another's.
- At every stopping point: commit + push (container is ephemeral).
- Escalate to the human operator (not silently guess) when: a review
  contains a threat/legal/medical-emergency claim, a draft can't pass
  compliance after retries on a sensitive review, or a practice asks
  for something outside this runbook.

## State of the build
Phase 1 (engine + console + HIPAA gate + per-practice config) AND
Phase 2 (approval state machine + per-practice persistence + 3-channel
rendering + working magic-link approval page + simulated Google
post-back, tested end-to-end offline) are **built**. Run it via the
console: draft → "Send batch for client approval" (delivers on the
practice's channel; auto-approves opted-in positives) → client approves
on the magic-link page (or bulk-approves positives) → "Post approved"
(simulated until Google access is granted). Only credential-gated swaps
remain: Google Business Profile API + per-practice OAuth, and real
SMTP/Twilio behind the `Sender` protocol — no design work left. See
`review-drafter/SPEC.md`; that spec + this runbook are source of truth.
