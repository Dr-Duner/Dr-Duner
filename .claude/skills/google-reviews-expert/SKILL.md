---
name: google-reviews-expert
description: Use when working with Google reviews — Google Business Profile API integration, review/reply mechanics, star math, local-pack ranking impact, or Google's reply content policy. For the Review Response Drafter's Google integration and for sales claims about review ROI.
---

# Google Reviews Expert

Authoritative operating knowledge for how Google reviews work. Used for
phase-2 integration and for accurate sales claims.

## CRITICAL: verify before coding
Google's API surface changes and the old "Google My Business API" was
split into the **Business Profile APIs**. Before writing integration
code, fetch current Google docs and confirm: exact API name, endpoints,
OAuth scopes, quota. Do NOT hardcode from memory. Treat the notes below
as orientation, not gospel.

## API orientation
- Reviews + replies live under the Business Profile APIs (the
  account/location → reviews resource). Reading reviews and posting a
  single reply per review is supported; one reply per review (updating
  replaces it).
- Auth: OAuth 2.0, the practice owner grants access to *their* location.
  Access to the API historically requires a Google approval/allowlisting
  step — start that application early (it has lead time).
- No realtime push for reviews; design for polling on a schedule.
- Quotas are low by default — batch, cache, request more if needed.

## Review mechanics that matter for sales
- Star rating shown is an average of all reviews; recent volume and
  recency influence prominence.
- Responding to reviews is a public, owner-side action; Google
  encourages it and review activity/engagement correlates with local
  visibility (the "local pack").
- Reviewers can edit reviews — a good reply often nudges rating upward.
- Reviews with owner replies signal an engaged business to prospects.

## Google reply content policy (enforce in drafts)
A reply can be removed / hurt the profile if it contains: spam,
off-topic content, harassment, personal/confidential info, or
conflicts of interest. For dentistry this stacks with HIPAA — see the
`hipaa-review-compliance` skill, which is stricter and takes precedence.

## Sales-ready facts (use, don't overstate)
- More recent positive reviews + owner responses → stronger local
  presence and higher click/call rates. Frame as "reputation velocity."
- Unanswered negative reviews are the visible risk we remove.
- Yelp gap: Yelp's Fusion API returns only ~3 truncated review
  excerpts and scraping violates Yelp ToS — v1 is Google-centric;
  Yelp is manual paste only. Set this expectation with practices.
