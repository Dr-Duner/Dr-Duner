---
name: business-operations
description: Use for the business mechanics of running the Review Response Drafter solo — pricing, billing, contracts, support cadence, metrics, what to automate vs. escalate to the human operator. The "one-man-shop" operating layer above the service runbook.
---

# Business Operations

The layer above delivery. `service-operator` runs the service per
practice; this runs the *business*. Built for one person — automate the
routine, escalate the legal/financial/judgment calls to the human
operator.

## Pricing & packaging
- Value-priced, not cost-plus (API cost ~$1–3/practice/mo). Anchor on
  hours saved + HIPAA risk removed (`dental-practice-marketing`).
- Simple monthly tiers by review volume. One page, no custom quotes in
  v1. Free first week on real reviews (the trial is the sales engine).
- Raise price by tier as volume grows; don't reflexively discount —
  trade price holds for the free trial instead.

## Billing
- Simple recurring monthly (a standard payment processor). No usage
  metering in v1 — predictable for the practice, simple for you.
- ESCALATE to the human operator: connecting or configuring any
  payment account, refunds, chargebacks, price changes for an existing
  customer, anything touching money movement. Never auto-handle funds.

## Contracts & compliance (ESCALATE — do not self-author)
- A simple services agreement + the data-handling/PHI terms (BAA path)
  must be human/counsel owned before any paid customer. Flag as a hard
  launch-blocker; surface it, don't draft binding legal terms solo.
- Keep the compliance one-pager current (mirror
  `hipaa-review-compliance`); offer it proactively to prospects.

## Support
- One channel (email). Target: reply within 1 business day.
- Most "support" is voice-profile tuning → loop `practice-onboarding`.
- Weekly recap per practice is the proactive retention touch
  (`service-operator`). Churn signal = practice stops approving;
  reach out human-to-human fast.

## Metrics that matter (review weekly)
Funnel: leads sourced → contacted → engaged → demo'd → trial → won
(`lead-pipeline`). Service: reviews handled, % approved un-edited
(quality proxy), turnaround time. Business: active practices, MRR,
churn, time you spent (the point is leverage, not a second job).

## Automate vs. escalate
- Automate: sourcing, drafting, compliance gate, queue delivery,
  recaps, pipeline updates, content drafting, follow-up reminders.
- ESCALATE to human: money movement, legal/contract/PHI terms, Google
  API approval submissions, posting replies (human-in-loop v1), any
  review with a threat / legal claim / medical emergency, anything
  outside these skills.

## Cadence
Daily: fire due pipeline next-actions, draft/queue, content.
Weekly: funnel + service + business metrics snapshot, recaps, pipeline
prune. Always: commit + push every stopping point (ephemeral container).
