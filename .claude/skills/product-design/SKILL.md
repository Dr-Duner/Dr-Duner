---
name: product-design
description: Use when designing the Review Response Drafter's product and UX — the internal operator console for reviewing/posting gated drafts, the practice onboarding flow, and the sales demo. The client is never a UI user; the operator is.
---

# Product Design

This is a **fully managed service**, not self-serve software. There are
two surfaces: (1) an **internal operator console** where we QA gated
drafts (operator is the only user); (2) a **lightweight client approval
surface** — the practice approves before anything posts, on the channel
they chose. The practice never logs into an authoring app and never
writes or posts; they just tap approve. This skill specifies the UI;
the Phase-1 console is built (see `review-drafter/SPEC.md`).

## Design principles
- Operator console optimizes **throughput**: many practices' gated
  drafts QA'd and routed fast; show *why each draft is HIPAA-safe*
  inline.
- Client approval surface optimizes **near-zero friction**: a busy
  office manager approves in seconds, from their phone, no login, no
  app to learn. The approval is a deliberate consent action (liability
  anchor) but must feel effortless.
- Nothing posts without client approval (explicit for 1–3★; bulk or
  opt-in-auto for 4–5★). Never a client authoring app. Never autonomous
  unless a practice explicitly opts into auto-approve-positives.
- Other client-facing surface = a clean weekly proof-of-work recap and
  a smooth one-time onboarding. Nothing else.

## Client approval surfaces (all three, practice picks one)
- **Email digest (default):** batched pending replies; each shows the
  review + the reply + a one-line "HIPAA-safe ✓" reassurance; one-click
  **Approve / Edit / Reject** links (tokenized, no login). 4–5★ grouped
  with a single **Approve all positives** button; 1–3★ listed
  individually, each requiring its own tap. Mobile-first; skimmable in
  under a minute.
- **Magic-link page:** one tokenized URL → a single page, same content
  and grouping as the digest, with inline edit boxes. No account.
- **SMS:** one text per 1–3★ reply (review snippet + proposed reply +
  "reply YES to approve, NO to reject"); a daily "N positive replies —
  reply OK to approve all" for 4–5★. For edits, SMS falls back to
  "reply EDIT to get a link." Keep within sensible message limits.
All three: never expose PHI beyond the public review text; tokens
expire; an un-actioned reply is held, never auto-posted (unless the
practice opted into auto-approve-positives).

## Operator console spec (built — a 4-step pipeline)
The console reads as one linear pipeline: **1 Draft → 2 Send for
client approval → 3 (client approves on their channel) → 4 Post
approved**. No operator self-approve anywhere — the operator only QA's
and dispatches.
1. **Intake bar:** practice select + paste/CSV → "1 · Draft replies";
   confirms "Found N — M positive, K need explicit approval".
2. **QA card:** route badge, reviewer/stars/date, review text, the two
   gated variants as **radio-selectable** editable boxes + "✓ why safe"
   + Copy. The operator picks/edits one; that is all they decide.
3. **Dispatch panel** (after Send): channel + recipient, the prominent
   **client approval link** (copy/open — operator can preview-as-client),
   a collapsible "exactly what the client receives", and a live
   **queue status** readout (pending/approved/posted/rejected).
4. A sibling **/prospect** page: lead qualifier + free-sample
   generator for outbound (`lead-generation`).
Persisted store is the operator record (no CSV export needed).

Non-negotiable rules:
- No draft shown until it passes the compliance gate.
- Posting always requires client approval (explicit 1–3★; bulk/opt-in
  4–5★). Negatives visually flagged, never bulk-approvable.
- Editing never loses the original. Re-run the gate on edited text. No
  PHI persisted in Phase 1.

## Onboarding flow (one-time, per practice — minimal client effort)
Drive `practice-onboarding`: capture voice (paste past replies OR the
6-Q form), office phone, sign-off, the **approval channel + approver
contact**, the optional **auto-approve-positives** choice, AND the
Google OAuth grant + written authorization. Confirm the voice back once
("Does this sound like you?"). After this the client only ever taps
approve.

## The demo (sales asset)
30-sec: a nasty 1★ review → safe warm draft with the why-safe note →
a one-tap approve on the phone → posted. Framing: "we write it and post
it — you just tap yes; positives we can even bundle." (`sales-closing`
uses it.)

## Anti-goals
No client authoring app. No vanity dashboards, no AI jargon, no
autonomous posting unless explicitly opted in. The client's "product"
is: we do all the work, they tap approve, weekly proof-of-work recap.
