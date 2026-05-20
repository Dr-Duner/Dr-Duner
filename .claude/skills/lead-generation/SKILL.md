---
name: lead-generation
description: Use for the mechanics of finding and sourcing dental-practice leads — building qualified target lists, identifying review-pain signals from public data, scoring them, and producing the free-sample weapon. The top of the funnel.
---

# Lead Generation

Find dental practices whose *public* review situation proves they need
this, score them, and hand outreach a ready weapon. Messaging lives in
`cold-outreach-dental`; pipeline tracking in `lead-pipeline`. No Google
API is needed for any of this — it is the pre-API revenue engine.

## The daily motion (operational)
1. **Source** 15–25 practices/day from public maps/search in one metro
   at a time (a city's "dentist" search = the universal list).
2. For each, eyeball the public Google profile and record the
   non-clinical signals (below). 60 seconds per practice.
3. **Score** with the qualifier (`app/leads.py` / the `/prospect`
   page): enter the signals → HOT / WARM / COLD + the exact opener
   line. Work HOT first; WARM in slow periods; drop COLD.
4. For every HOT, paste 3–6 of their *real* reviews into `/prospect`
   → it returns the **free-sample pack** (real HIPAA-safe replies to
   their own reviews). That pack IS the cold email body.
5. Hand the row + score + opener + sample to `cold-outreach-dental`.

Target: ~10 qualified HOT/WARM with samples per working day. Quality
over volume — this is a trust niche; a spam reputation kills it.

## The qualifying signals (public, non-clinical only)
Read these straight off the listing — never patient/clinical facts:
- **recent 1–2★ with no owner reply** — hottest; visible bleeding.
- **count of recent reviews left unanswered** — ongoing pain.
- **total review volume** (≥50 = continuous, recurring value).
- **avg rating < 4.0 while negatives sit unanswered** — urgent.
- **existing replies look templated/robotic** — they care but do it
  badly → easy to displace (warm, not hot).
The qualifier weights these deterministically; trust its tiering.

## Where leads come from (ranked)
1. Public maps/search by metro — the universal source.
2. Inbound from content (LinkedIn/X DMs) — highest intent; prioritize.
3. Referrals from happy practices (ask explicitly; dentists know
   dentists).
4. Office-manager communities — presence, not scraping.

## The free-sample weapon
The single highest-converting asset. It is *their* reviews, answered,
HIPAA-safe — proof not pitch. Generate via `/prospect`; if no API key
the replies are safe templated fallbacks (still HIPAA-clean — say so
honestly, and that the paid product matches their voice). Lead the
sample with their scariest negative: that is the reply they are most
afraid to write themselves.

## Pre-Google-API revenue (do not wait for the API)
Google API access has lead time; the business earns before it lands:
- **Concierge trial:** we draft + HIPAA-gate + the practice approves;
  then *they paste* the approved replies into their own Google
  dashboard (or grant us delegated access to their own dashboard).
  This is NOT automation and NOT a ToS issue — it's them replying with
  our help. Removes the real pain (writing + compliance fear + time)
  with zero API dependency. Price it as a paid trial → monthly.
- When API access lands, the same practices upgrade silently to
  auto-ingest + post-on-approval. No re-sell.

## List hygiene & law
Public business data only (name, public site/email, phone, city,
review count, avg rating, "recent unanswered? y/n", source, date,
signal note). Dedupe — one row = one practice. Obey CAN-SPAM / local
anti-spam: low volume, real personalization (use the sample + opener),
honest sender, easy opt-out.

## Output per lead
Qualified row + tier/score + the one specific public observation
(opener) + the generated free-sample pack → `lead-pipeline`.
