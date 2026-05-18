---
name: lead-generation
description: Use for the mechanics of finding and sourcing dental-practice leads — building qualified target lists, identifying review-pain signals from public data, and feeding outreach. The top of the funnel.
---

# Lead Generation

Find dental practices whose *public* review situation proves they need
this. Outreach messaging lives in `cold-outreach-dental`; pipeline
tracking in `lead-pipeline`. This skill is sourcing + qualifying only.

## Where leads come from (ranked)
1. **Public maps/search of dental practices by area** — the universal
   source. For each: name, site, phone, # of Google reviews, average
   rating, and the key signal below.
2. **Inbound from content** — LinkedIn/X DMs (`linkedin-content`,
   `social-media-marketing`). Highest intent; prioritize.
3. **Referrals** from happy practices (ask explicitly; dentists know
   dentists).
4. **Dental office-manager communities** — presence, not scraping.

## The qualifying signal (the pitch is in the data)
Rank a practice HOT when its public profile shows review pain:
- recent reviews with **no owner reply** (visible gap), and/or
- recent **1–2★ reviews unanswered**, and/or
- high review volume but sparse/robotic existing replies.
Only ever use **public, non-clinical** facts. Never patient info.

## List-building rules
- Capture only public business data: practice name, public email/site
  contact, phone, city, review count, avg rating, "unanswered recent
  reviews? y/n", source, date added.
- Respect platform ToS and anti-spam law (CAN-SPAM / local equivalents):
  low volume, real personalization, easy opt-out, honest sender. This
  is a trust niche — a spam reputation kills the business.
- Dedupe; never load the same practice twice. One row = one practice.
- Hand qualified rows to `lead-pipeline` with the signal noted, so the
  first outreach line can reference their actual public review gap.

## Volume posture
Quality over quantity: a small list of well-qualified practices with a
real, referenceable review gap converts far better than mass blasts —
and protects deliverability and reputation.

## Output
A clean qualified-lead row per practice (fields above) + the one
specific public observation that the outreach opener will use.
