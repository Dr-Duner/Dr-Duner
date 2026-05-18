---
name: lead-pipeline
description: Use to track and nurture leads through stages for the Review Response Drafter — a lightweight one-person CRM operating model with stages, follow-up cadence, and the handoffs between lead-generation, cold-outreach, and sales-closing.
---

# Lead Pipeline

The connective tissue so no lead is dropped — built for a one-person
shop, so it must be lightweight and fully trackable in a single file/
table. Sourcing = `lead-generation`; messaging = `cold-outreach-dental`
/ `linkedin-content`; closing = `sales-closing`.

## Stages
1. **Sourced** — qualified row exists (from `lead-generation`), not yet
   contacted.
2. **Contacted** — first touch sent (note channel + date).
3. **Engaged** — they replied / showed interest.
4. **Demo'd** — free batch of drafted replies delivered.
5. **Trial** — using it (free week).
6. **Won** — paying.
7. **Lost / Nurture** — no for now; reason recorded; revisit later.

## Tracked fields (one row per lead)
practice, contact, channel, signal (the public review gap), stage,
last_touch_date, next_action, next_action_date, notes, source.

## Follow-up cadence (don't over-chase a trust niche)
- Contacted → no reply: 1 gentle follow-up at day 3–4, a second at day
  8–10, then move to Nurture. Max 3 total touches. Never more.
- Engaged → deliver the free batch fast (same/next day). Speed closes.
- Demo'd → follow up within 2 days with the simple price + trial offer.
- Trial → check in mid-trial (helpful, not pushy) and at trial end.
- Always set an explicit `next_action` + date on every row, every time.
  A row with no next action is a dropped lead.

## Operating rules
- Single source of truth (one CRM file/table); update it every touch.
- Persist + commit it (container is ephemeral — a lost pipeline = lost
  revenue).
- Keep per-lead notes factual; never store any patient/clinical info.
- Weekly: review every Contacted/Engaged/Demo'd row, fire due
  next_actions, prune stale to Nurture. Report a one-line funnel
  snapshot (counts per stage) to the operator.

## Handoffs
Sourced→Contacted uses `cold-outreach-dental`/`linkedin-content`.
Demo'd→Won uses `sales-closing`. Won triggers `practice-onboarding`
then `service-operator` for delivery.
