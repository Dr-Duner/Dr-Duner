# Lyra — Art Direction A/B (chibi vs. stylized adult)

Status: **PLAN ONLY** — awaiting Gee's credit go-ahead before any
generation fires. This file defines the test so the choice is
template-wide and made on evidence, not vibes.

## Why we're testing
- Locked direction (CLAUDE.md, DESIGN §3c-1): **chibi 2.5D**, App
  Store quality. Distinctive, brand-friendly, but chibi by
  definition leans cute.
- Gee's intent (2026-05-20): coaches are "practical, intelligent,
  interesting — *not cutesy*. Users develop a relationship with
  this coach; they bond with the coach so they keep coming back."
- The relationship is the retention engine. If the art style works
  *against* gravitas, the bond is harder to build. We test one
  Lyra render in each direction and pick on look-and-feel before
  locking the template for all 4 coaches × 20 lessons.

## The test
Two Lyra key stills, **identical scene**, identical palette, identical
prompt scaffolding. Only the art direction varies.

### Scene (constant in both renders)
- Lyra at a bronze telescope on a whitewashed marble terrace
  overlooking the Aegean at dawn.
- Modern phone on the marble ledge, glowing signal-green `#00c896`.
- Strict palette: phone/app surface = black `#000000` + signal
  green; everything else = full-color real Aegean (whitewashed
  stucco, bright blue sea, sun-warm marble, dawn sky).
- 9:16 vertical, App Store quality.

### Variant A — **Chibi** (current locked direction)
- ~2.5 heads tall, slightly oversized head, soft round features.
- Reference: locked Lyra still, job
  `a777c0e0-195e-46f0-b9ae-11b4e45c9b66`.
- Tone: charming, approachable, mascot-friendly.

### Variant B — **Stylized adult** (proposed alternative)
- Realistic adult proportions (~7 heads tall), 2.5D illustrated,
  not photoreal. Think modern animated feature with painterly
  Mediterranean light — *grown, intelligent, calm*.
- Identity unchanged: same hair, same chiton/himation, same
  bronze telescope, same calm focused expression.
- Tone: someone you would trust with your money.

## Decision criteria (the rubric)
Score each variant on these dimensions; pick the higher total.

1. **Bondability** — can a real user believe they'd build a long-term
   relationship with this coach? (0–5)
2. **Trust with money** — does this person look like someone you
   would take options advice from? (0–5)
3. **Distinctiveness** — does it stand out in an App Store screenshot
   row? (0–5)
4. **Brand fit** — ancient world + modern phone dichotomy still
   reads instantly? (0–5)
5. **Production cost & reuse** — will it animate well across 20
   lessons × 4 coaches without falling apart? (0–5)
6. **Coach voice fit** — sits with "warm low female register,
   unhurried, grounded, calm authority"? (0–5)

## Cost
Two image generations (key stills), nano_banana_2-class model, 9:16.
Single-digit credits each — well under 10 cr total. No video.

## Decision flow
1. Gee approves the credit spend in chat.
2. Generate Variant A and Variant B in the same model with identical
   prompt scaffolding (only the proportions/style line differs).
3. Display both via `job_display`, score against the rubric in this
   file, and commit the scored grid + decision into DESIGN §3c-1.
4. If A wins: CLAUDE.md and DESIGN §3c-1 chibi lock stays in force.
5. If B wins: CLAUDE.md and DESIGN §3c-1 update to "stylized adult,
   not chibi" — template-wide for all 4 coaches × 20 lessons.

## Note on the existing locked Lyra still
The current locked Lyra still
(`a777c0e0-195e-46f0-b9ae-11b4e45c9b66`) is Variant A. If B wins, that
still is retired and a new Variant B still becomes the locked
template identity for Lyra.
