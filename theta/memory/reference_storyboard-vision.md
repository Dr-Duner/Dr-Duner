# reference_ Storyboard vision

**LOCKED 2026-05-18 (Gee).** Canonical structure for coach videos.

- World: Ancient Greece; 4 coaches are friends/neighbors/family in
  ordinary Greek life.
- Style: CHIBI animated characters.
- Beat: everyday scene -> unexpected modern smartphone BUZZ (the
  anachronism is the signature hook) -> chibi coach reads MONO text
  (IBM Plex Mono) -> scanner UI rendered EXACTLY like the real app
  -> trade ideas -> CTA + Theta Θ logo.
- Per-coach everyday scene: Lyra = telescope at dawn (locked);
  Nestor = training/Spartan drill (locked); Chiron = TBD; Atlas = TBD
  (Gee defines later).
- SCOPE LOCKED: universal spine — (a) template for ALL lesson videos
  1–19, (b) recurring wrapper around each lesson's teaching middle,
  (c) the marketing format.
- BRAND ESSENCE LOCKED: ancient and modern at the same time; Theta
  makes trading modern and usable today.
- Hard dependency: in-video scanner/message UI must equal the real app
  UI (DESIGN.md §3b/§3c). Video and app are coupled — design together.
- Example render: theta/storyboard-vision-nova.png (+ .mmd).

## Generated assets (job IDs — re-display via job_display)
Network policy blocks the image-host domain, so generated media can NOT
be curled into the repo. Persist job IDs here; future sessions re-open
them with the generation tool's job_display.
- Lyra chibi key still (cold-open + buzz, locked scene), 2026-05-18,
  nano_banana_2, 9:16, ~2 credits each:
  - Option A: job `a777c0e0-195e-46f0-b9ae-11b4e45c9b66`
  - Option B: job `47efdc27-b9b7-4b11-a869-d3f014e8a90c`
  - Canonical pick: **Option A** — job
    `a777c0e0-195e-46f0-b9ae-11b4e45c9b66` LOCKED 2026-05-18 (Gee).
    Lyra's official chibi identity for all 19 lessons; match
    proportions/palette/scene to it in every future Lyra generation.
- Lyra proof clip (Shot 1→2 cold-open + buzz), 2026-05-18,
  seedance_2_0_fast, 9:16, 480p, 4s, 6 credits, start_image = locked
  still: job `f7f11d9d-6b04-45fc-9aaa-d23775ad566c`. Silent (VO is a
  separate step). Re-display via job_display.
- Lesson 1 stills storyboard (7 key-frames, one per shot), 2026-05-18,
  nano_banana_2, 9:16, 1k, ~2 cr each, identity ref = locked still A.
  Maps 1:1 to `lesson1-script.md` shots. Re-display via job_display:
  - S1 cold-open: `8cc62c94-198a-44be-a10b-e4099fb52f88`
  - S2 the buzz: `f8b262ee-f6d3-4991-82c3-83d6095f782e`
  - S3 the read (mono): `21d422dd-b1fd-4519-8d17-ab8cac9840c4`
  - S4 teaching A: `2cef1c82-6367-4847-bad0-3831a308bd9d`
  - S5 teaching B: `29324721-36bd-4bfc-8a52-cd559eb8e2b3`
  - S6 the scan (app UI): `8b8179a2-ffce-411f-b321-117a1e9ce87e`
  - S7 coach land + Θ CTA: `649619ad-ad6e-4c3b-a180-4a556966d1bb`
    (end hook LOCKED 2026-05-18 Gee: "Θ / don't predict it. trade
    it. now." — supersedes old S7 `b5b93023…` / "trading, made
    usable today"; the dropped line is retired everywhere)
- **Lesson 1 all-black redo — WRONG ENVIRONMENT, scrap, 2026-05-18**,
  nano_banana_2. Misread the palette rule: put black behind the
  *scene* too. Per the TWO-REGISTER refinement (DESIGN §2, "Black
  brand cards", Gee), scene = bright Aegean; only brand/terminal
  surfaces are black. These all-black renders are NOT usable as
  scene frames — anchor `1e1e016f`, S1 `e206e9c3`, S2 `b9f4867e`,
  S3 `b646b750`, S4 `e2fd6c12`, S5 `6d259ad6`, S6 `cb5f48ab`.
  (a777c0e0 stays the face/proportions source of truth.)
- **Lesson 1 CORRECT redo — IN PROGRESS (funded, 2026-05-19).**
  Two registers per shot:
  - **CANONICAL LYRA IDENTITY ANCHOR — LOCKED 2026-05-19 (Gee):
    job `9af9b0c3-298b-43c8-b2f0-62d1af490395`.** Full-color real
    Aegean (whitewashed Cycladic stucco, bright blue sea, sun-warm
    marble, dawn), phone the only modern/black-green object. This
    is Lyra's official identity for the WHOLE product — ref it for
    every Lyra scene frame, all 20 lessons. (a777c0e0 = navy-era
    face/proportions source only; 9af9b0c3 supersedes it on-spec.)
  - S1 cold-open, S2 buzz, S5 sort, S7 coach-land = Aegean world.
  - PHONE-SCREEN INVARIANT (Gee 2026-05-18): whenever the phone
    screen is shown it must be PIXEL-FAITHFUL to the real shipping
    app terminal — DESIGN §3b-1 + approved render
    `96e246fb-6404-44f9-a844-a0cd245091c4`: pure black, IBM Plex
    Mono, constant `[<username>@theta ~] %` prompt, off-white
    majority text, cyan `[LYRA]` tag, green ONLY on a `+delta`,
    amber `!` alert, blank-line-per-block spacing,
    `[ PAPER TRADE ] [ OPEN BROKERAGE ]` action line. The in-video
    screen IS the app screen — never a bespoke title card. "The
    screen looks exactly like the app when they get a message."
  - S3 the read = phone fills frame, screen = that exact terminal
    with the THETA message arriving in the terminal flow; Lyra's
    face at edge in-world (Aegean behind the phone).
  - S4 = Aegean, but the Epictetus quote on a black lower-third.
  - S6 the scan = the exact terminal scanner card (per the
    invariant above), full-frame brand register.
  - S7 closing Θ CTA = cut from Aegean coach-land to a pure-black
    brand card for the locked lockup "Θ / don't predict it. trade
    it. now." (hook still LOCKED, unchanged).
  - **GENERATED 2026-05-19, two-register on locked anchor 9af9b0c3
    (PENDING GEE REVIEW — prototype quality bar for all 80 videos):**
    - S1 cold-open (Aegean): `263a22ee-881e-4056-8d42-18602fd0c10b`
    - S2 the buzz (Aegean): `d1f92463-39a5-42e3-bde8-0675c23973ec`
    - S3 the read (black app screen + Aegean edge):
      `3bcdffa9-9b99-4109-b13c-3646a4031063`
    - S4 teaching A (black screen + Aegean inset):
      `15f91bad-bf67-478a-8027-37f63df2c4c0`
    - S5 teaching B sort (Aegean, marble stones):
      `bdfad99b-fede-4917-9e9b-7037808f20f1`
    - S6 the scan (full black terminal card):
      `5606932e-80cc-4499-8b97-db755ccc78f9`
    - S7 Θ CTA (black brand card):
      `76ac35f4-1554-423d-80e5-d6691414dc41`
  - **v2 alternates (2026-05-19, tightened text + face):** S1
    `179535c2`, S2 `14ac24a0`, S3 `19dd0773`, S4 `f7b44c44`, S5
    `f778a953`, S6 `3c6a267c`, S7 `cc9c25c3`.
  - **GEE PER-SHOT VERDICT 2026-05-19 (LOCKED picks):**
    - S1 = v2 `179535c2-4063-4858-8c6c-7a540e85c46a`
    - S2 = v1 `d1f92463-39a5-42e3-bde8-0675c23973ec`
    - S3 = v1 `3bcdffa9-9b99-4109-b13c-3646a4031063`
    - S6 = v1 `5606932e-80cc-4499-8b97-db755ccc78f9`
  - **REDO QUEUE (Gee 2026-05-19):**
    - S4: overloaded ("makes no sense") — a 9s morph crushed into
      one frame. Redesign to a single clear frame; direction TBD
      (options: clean PROCESS|OUTCOME split / sky→chart thesis /
      pure quote card / cut S4 from template).
    - S5: register violation — modern trading words were carved in
      ancient marble. MOVE to the BLACK APP REGISTER: the
      CONTROL-vs-NOISE sort happens on the phone screen (black,
      IBM Plex Mono), Lyra reacts in the warm Aegean around it.
    - S7: regenerate as v3 = v2's clean correct text/hook at v1's
      bigger Θ scale.
  - **v3 redos GENERATED 2026-05-19 (pending Gee verdict):**
    - S4 v3 clean PROCESS|OUTCOME split, black app register
      (chosen direction; 1st gen failed, retried):
      `8af19b07-091c-4cb6-a9ad-991ae07e54de`
    - S5 v3 sort on phone screen + Lyra in Aegean:
      `847e2f80-7c7b-4a83-8ad8-82c33c3e9de8`
    - S7 v3 big Θ + clean hook:
      `625fa509-e079-4f28-b8ad-4031dcdde522`
  Old navy S1–S7 (`8cc62c94…`/`f8b262ee…`/`21d422dd…`/`2cef1c82…`/
  `29324721…`/`8b8179a2…`/`649619ad…`) and the all-black scrap set
  remain retired.
- Terminal HOME screen render (DESIGN 3b-1), 2026-05-18,
  nano_banana_2, 9:16, 1k, ~2 cr: job
  `c78dd19f-1930-40f3-9067-78b63c1c6b6d`. Tight block, +$ delta in
  signal green, paper/brokerage buttons. First visual of 3b-1.
  (SUPERSEDED — was navy + dense.)
- Terminal HOME screen v2 — black + readable spacing + real
  scanner feed (DESIGN 3b-1 current), 2026-05-18, nano_banana_2,
  9:16, 1k, ~2 cr: job `96e246fb-6404-44f9-a844-a0cd245091c4`.
  Pure black bg, cyan [LYRA]+scan, green +delta, amber ! alert,
  blank-line-per-block. Canonical 3b-1 visual.
