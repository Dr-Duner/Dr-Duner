# THETA — Living Design Doc

This is the single home for app, game-interface, character, marketing, and
video decisions. We chat here. It is committed every session so it survives
the ephemeral container. Nothing below is final unless marked **LOCKED**.

> **CONTEXT BOUNDARY — read first.** Claude Code (this tool) has NO access
> to Cowork, the simulator, voice chats, or any other session. It only sees
> what is committed to this repo. Decisions made anywhere else MUST be
> written into this doc or they are lost to future sessions. Rule: a
> decision isn't real until it's a line in this file.

---

## 1. The Pitch (one paragraph)
Theta teaches Stoic discipline applied to live options markets. The user
picks one of four coaches (a character with an ancient-world identity and a
modern phone). The coach is the emotional spine: silent-but-watching early,
then earns a single spoken line at the first real paper trade, then goes
fully live with a real-time scanner. **The coaches' videos + characters +
real-time data in a game format are the product.**

**Brand essence (LOCKED 2026-05-18):** ancient and modern at the same
time. Theta takes trading and makes it modern and usable today. The
signature image is everyday Ancient Greek life interrupted by a modern
Theta trade scan.

## 2. Locked Decisions
- **LOCKED** Brand name: Theta (symbol Θ).
- **LOCKED** Palette — DELIBERATE DICHOTOMY (REFINED 2026-05-18, Gee).
  WHY: the color split *is* the message. The phone/app is modern tech
  dropped into the ancient world; black/green/off-white vs full-color
  antiquity makes that contrast felt, not explained. It also rhymes
  with Lesson 1's Dichotomy of Control — two worlds, one frame.
  1. **The phone/app interface = ONLY black/green thing**: pure black
     `#000000`, signal green `#00c896` (= Θ mark + reserved gain delta
     only), off-white `#eef6f3` text, red = reserved loss delta only.
     This covers the phone screen, the app UI, the logo, and any
     full-screen "the app talking" moment (text/quote beats, closing
     Θ CTA card) — those ARE the app shown full-frame. Navy `#0b1f3a`
     retired (never use).
  2. **Everything else = full-color real Aegean**: whitewashed
     Cycladic stucco, bright blue sea, sun-warm white marble, dawn
     sky, period-accurate ancient Greece. NOTHING here is black/green.
     The phone is the single modern object in the world.
  Cut between the two registers (warm antiquity ↔ cold device). Black
  scene backdrops were a misread — redo. Earlier all-black renders
  (Lesson 1 anchor + S1–S6) are wrong-environment, scrap.
- **LOCKED** Four coaches: Lyra (Analyst), Nestor (Veteran), Chiron (Patient
  Teacher), Atlas (Risk Manager). Identities in `lesson-flow.mmd`.
- **LOCKED** Arc: Lesson 1 (Dichotomy of Control) → 2–19 (mindset + craft)
  → first paper trade closes → coach's one line → Lesson 20 scanner unlock.
- **LOCKED** Lesson 1 video concept: see `lesson1-storyboard.png`.
- **LOCKED** Production scope & budget (Gee, 2026-05-19): **Premium
  full product** — all 20 lessons, ALL 4 coaches, fully animated at
  Kling-grade motion. Target: finish inside the 90-day window.
  Budget plan ≈ **1,500 credits** total; funded by a **2,000-credit
  top-up ($95)** plus the ~600 credits from monthly resets across the
  window (200/mo, anchor ~the 10th). Cost is controlled by the
  template reuse model: per-coach wrapper (S1/S2/S3/S7) generated
  ONCE per coach and reused across all 20 of that coach's lessons;
  teaching middle (S4/S5) + SCAN card are coach-agnostic, generated
  ONCE and reused across all 4 coaches.
- **S4/S5 reframe — LOCKED 2026-05-19 (Kevin), REVISED 2026-05-19
  (Kevin) — paper-trade flow. SUPERSEDED 2026-05-20 by the
  "Lesson = app demo = promo" lock below — see that entry. The
  S4/S5-only framing is no longer authoritative; the whole 7-shot
  wrapper now reflects the app-execution spine.**
- **Lesson = app demo = promo — LOCKED 2026-05-20 (Gee).**
  Kevin's plausibility-check conversation collapsed the false
  promo-vs-lesson split. The L1 cut (and every lesson's wrapper)
  is simultaneously: the lesson, the product demo, and the
  elevator pitch. It shows the three pillars in 40s — **coach
  relationship** (Lyra opens + closes), **scanner** (the terminal
  home screen with the daily `[COACH] scan` block; trades surface
  matching the user's strategy), **frictionless paper-trade
  execution** (notification → scanner → pick underlying/stop/TP →
  review → send → Θ). Two initial sell points: (1) the scanner
  surfacing trades matching the user's strategy, (2) how dead-easy
  execution is once the scanner has shown them. The lessons that
  *generate* the strategy parameters live elsewhere in the arc and
  are OUT OF SCOPE for the wrapper. Template-wide for all 20
  lessons; see new FIXED WRAPPER in `LESSONS.md`.
- **Execution path — LOCKED 2026-05-20 (Gee): PAPER-TRADE ONLY at
  launch.** The "send" beat in every lesson video and in the app
  v1 is a *simulated* order, not a real broker order. On-screen
  `PAPER TRADE` badge is non-removable. Phase 2 (real-money
  execution via broker partnership or hand-off) is a separate
  decision deferred to post-launch. See `COMPLIANCE.md` for the
  full posture and the rules this locks in for marketing copy
  and on-screen framing.
- **Coach art direction — UNLOCKED 2026-05-20 (Gee): chibi vs.
  stylized adult pending Lyra A/B render-off.** CLAUDE.md and
  §3c-1 still describe chibi 2.5D, but the lock is on hold until
  the A/B test resolves. Gee's intent — "practical, intelligent,
  interesting — not cutesy" coaches users *bond with about money*
  — may not match chibi proportions. Test plan + criteria + cost
  in `lyra-art-direction-ab.md`. Awaiting credit go-ahead to
  generate Variant A (chibi, locked) and Variant B (stylized
  adult) Lyra key stills and pick on evidence. Top-up credits do not expire
  for 90 days — matches the window exactly.

## 3. Open Decisions (need your call)

### 3a. Typography  — **LOCKED**
- **LOCKED (Gee, 2026-05-18): coach-facing text = IBM Plex Mono.** The
  messages the customer reads after picking their agent render in this
  monospace computer-terminal face. The terminal aesthetic IS the
  interface voice. Free / OFL — no licensing cost in-app.
- Brand/Θ/lesson-title face (separate from coach text) still open — a
  second face is optional; terminal-only is a valid strong choice.

### 3b. The coach interface (post-selection)  — DESIGN NEEDED
After the user picks a coach, the interface IS the coach texting them in
"our font." Open questions: chat-style bubbles vs. full-screen lines?
Typing animation? Coach avatar still vs. short looping video? Voice/audio?

### 3b-1. Home screen = the terminal  — **LOCKED** (Gee, 2026-05-18)
The app's home/dashboard screen IS a Unix terminal readout. Same feel,
same IBM Plex Mono text as a real `zsh` window (ref: Gee's macOS
Terminal screenshot).

**APPROVED reference render (Gee: "That is perfect!", 2026-05-18):**
job `96e246fb-6404-44f9-a844-a0cd245091c4` — black bg, mostly
off-white text, cyan `[LYRA]` + scan, green `+delta`, amber `!`
alert, blank-line-per-block. This image is the canonical look;
match it for all future home-screen work.

**Design principle (locked):** read like real code — the *majority*
of text is plain off-white; color is rare and only ever means
something (coach identity, gain/loss, system alert). Never decorate
with color; color = signal.

**Username / prompt invariant (locked):** the shell prompt is
`[<username>@theta ~] %` where `<username>` is the user's own
handle (replaces the `trader` placeholder). It is **identical on
every screen and every session forever** — a constant prompt is
part of the brand, the thing that makes the interface feel familiar
and "theirs" the way a real terminal prompt never changes.

Top-to-bottom order:
1. `Last login: <Day Mon DD HH:MM:SS>` — the user's actual last
   session timestamp, verbatim terminal style.
2. Last-session recap: what they did + balance. The balance figure
   itself stays default off-white; the **± delta token (the sign +
   the amount, e.g. `+$340.00` / `-$120.00`) is colored signal
   green for a gain, red for a loss** — sign and number together.
3. Trading stats: trades entered (count) + win rate (%).
4. Coach block: coach's name + that day's scan, scan results listed
   in the same mono font (e.g. `[LYRA] daily scan — DD Mon`).
5. Bottom action prompt: paper-trade in-app, OR open brokerage to
   place a real trade. Two clear actions on a terminal prompt line.
Approved feel mock (text, not final art) — READABLE spacing
(REVERSED 2026-05-18, Gee: the ultra-dense one-line packing was too
condensed; you couldn't tell where one idea ended and the next
began). Now: blank line between logical sections, a label header
then indented aligned rows, ONE item per line:
```
Last login: Tue May 18 09:42:11 on theta

[trader@theta ~] % recap --last
  3 trades closed
  balance   $12,480.00   +$340.00
  entered 47   ·   win 61%

[LYRA] scan — 18 May   market: OPEN
  ! schwab token 0.0d — RE-AUTH

  holdings (2)
    DT    $38.64      HV%ile 100   vol ↑
    MELI  $1,556.31   HV%ile 100   ↓

  vspreads   none today  (profile: tighter-width)

  pipeline (4)
    MCO   $440.96   compounder, <50d MA, -4.9% wk
    SPGI  $414.33   compounder, <50d MA, -4.0% wk
    GPRT  …
    BPOS  $52.00    high-risk

[trader@theta ~] % _

  [ PAPER TRADE ]      [ OPEN BROKERAGE ]
```
Layout rule (supersedes the old "maximum density" rule): legibility
first. A **blank line separates each logical block** (recap / coach
header / holdings / vspreads / pipeline / prompt). Each block is a
lowercase label line, then **one record per indented line** with
**column alignment** so the eye scans down. Still a real terminal —
just spaced like a clean readout, NOT a jammed wall. Lists may cap
(e.g. top rows + `… n more`); scroll/expand handling still open.

**Coach terminal colors.** Each coach has a signature terminal
color; their name tag `[NAME]` AND their scan line render in that
color (everything else stays off-white #eef6f3):
- Lyra (Analyst) — cyan `#4fd1e6`
- Chiron (Patient Teacher) — soft blue `#6c8cff`
- Nestor (Veteran) — amber `#ffb000`
- Atlas (Risk Manager) — violet `#b18cff`
Status guard: signal green `#00c896` is RESERVED strictly for the
gain delta, and red strictly for the loss delta — NO coach uses
green or red (Gee, 2026-05-18, Lyra swapped off green so gains own
it cleanly). Signal green still lives in the app as the Θ mark /
brand accent, just never as a coach text color. The ± delta token
always wins and is never recolored to a coach color.
Ties to 3a (mono locked), 3c-1 (Θ terminal end card), and the L20
scanner-unlock arc. Sub-questions RESOLVED (Gee, 2026-05-18):
- Load: NO type-on animation. Readout appears instant, framed by a
  blinking cursor block at the top (after `Last login:`) and at the
  bottom prompt line. Calm, alive at both ends.
- Order: recap → stats → coach scan → action (as mocked). LOCKED.
- Bottom action default = **adaptive**: paper-trade is primary
  until the scanner unlocks at L20; after L20, open-brokerage
  becomes the primary action, paper stays available.

**Scanner block spec — real feed, terminal-skinned (Gee, 2026-05-18).**
Source = the existing "Capital Mind" Telegram bot daily-scan feed.
Same data, restyled into the §3b-1 house style: IBM Plex Mono,
black bg, `[COACH]` header + scan body in that coach's color, and
the READABLE spacing rule above (blank line per block, label then
one record per aligned line — NOT the old dense `|` packing).
Section → block mapping (Telegram → terminal):
- header: `DAILY SCAN — DATE` + `Market: OPEN` →
  `[LYRA] scan — DD Mon   market: OPEN`
- token/auth status (`SCHWAB TOKEN … RE-AUTH`) → its own system
  ALERT line prefixed `!`, amber `#ffb000` (status-warning role):
  `! schwab token 0.0d — RE-AUTH`
- `HOLDINGS ALERT (n)` → a `holdings (n)` label then one ticker per
  indented, column-aligned line.
- `VERTICAL SPREADS` → `vspreads   none today  (profile: …)`
- `PIPELINE — buy signals (n)` → a `pipeline (n)` label then one
  ticker per indented line; may cap with `… n more`.
Rule: directional ticks (vol ↑ / ↓, week %) stay coach color or
off-white — market direction, NOT the user's P&L, so they never
borrow the reserved gain-green / loss-red. Amber `!` is the sole
system-status role and overrides coach color on that line only.
(Canonical mock is the readable one above in this section.)

### 3c. Game format  — DESIGN NEEDED
What makes the lessons a "game": progress/XP, streaks, the locked scanner
as the prize, paper-trade scoreboard, the coach's trust meter? To define.

### 3c-1. Storyboard Vision  — **LOCKED** (Gee, 2026-05-18)
The canonical structure for the coach videos:
1. **World:** Ancient Greece; the 4 coaches are friends/neighbors/family
   living ordinary Greek life.
2. **Style:** CHIBI animated characters (locked).
3. **Everyday scene:** each coach shown individually mid–daily-life.
   - Lyra: at a telescope/astronomical instrument at dawn (locked).
   - Nestor: training / working out — Spartan drill (locked).
   - Chiron: everyday scene TBD (open — Gee defines later).
   - Atlas: everyday scene TBD (open — Gee defines later).
4. **Hook:** an unexpected modern smartphone BUZZES — "Theta has
   something for you." The anachronism IS the signature visual.
5. **The read:** chibi coach checks the device — MONO text (IBM Plex
   Mono) from their coach.
6. **The scanner:** a scanner message appears, UI rendered EXACTLY as
   the real phone app will look. (Dependency: app scanner/message UI
   §3b/§3c must be designed in lockstep — video and app are coupled.)
7. **Trade ideas** shown.
8. **CTA + Theta Θ logo** end card.
**Scope — LOCKED:** this is the universal spine. It is (a) the template
for ALL lesson videos 1–19, (b) a recurring wrapper around each lesson's
teaching middle (cold-open everyday life + buzz → lesson → Θ CTA), and
(c) the marketing format. **Brand essence:** ancient and modern at the
same time — Theta takes trading and makes it modern and usable today.
Renders: `storyboard-vision-nova.png` (concept),
`storyboard-production-template.png` (the video shot-by-shot +
App-Store quality bar), `storyboard-frame-layout.png` (9:16 grid /
in-app coach-UI language), `storyboard-L5-theta.png` (worked example).
All 19 lessons re-cut onto this template in `LESSONS.md`.

**Lyra canonical look LOCKED 2026-05-18 (Gee):** chibi key still, job
`a777c0e0-195e-46f0-b9ae-11b4e45c9b66` (nano_banana_2, 9:16). Telescope
at dawn, modern phone glowing signal-green on the marble ledge, strict
black/green/off-white palette. This is Lyra's official identity for all
19 lessons — match it in every future Lyra generation. Network policy
blocks committing the file; re-display via job_display by that ID.

**Lyra voice LOCKED 2026-05-18 (Gee):** kind but *deeper* — a warm low
female register, unhurried, grounded, calm authority; asks more than
tells; close-mic intimate. NOT the video model's job — VO is a separate
TTS/talent step composited over animation. Full script per shot:
`lesson1-script.md`.

### 3d. Lessons 2–19 treatment  — DRAFTED
- **Curriculum + per-lesson storyboards drafted:** see `LESSONS.md`
  (beat sheets) and `lesson-arc.png` (visual map). Built now from
  current knowledge; coach PRESENT + interactive throughout (this
  supersedes the old "coach silent 2–19" line — confirmed by Gee).
- **L9 is PROVISIONAL.** Real Lesson 9 was built in Cowork, seen in the
  simulator, and is the animation/automation bar. Not reachable here;
  swap the provisional L9 when Gee surfaces it (recording or written
  description of its animation + automation + how the coach appears).
- Open: refine individual lesson beats; render per-lesson visual
  storyboards (free) Lesson-1 style on request.

### 3e. Marketing  — IDEAS PARKED
User has several marketing ideas. Capture them here as raw bullets, shape
into a plan after the product spine is set.
- (add ideas here)

### 3f. Strategic backlog — surfaced 2026-05-20, not yet decided
Plausibility-check considerations raised in chat that need their own
decisions before they bite. Park here so they don't get lost.

1. **Coach AI / relationship layer (between lessons).** Gee's intent
   is users bond with the coach and keep coming back. Pre-rendered
   video alone won't bond. Realistic build: pre-rendered lessons +
   LLM-backed in-character chat with the same coach (Lyra/Nestor/
   etc. as Claude personas with locked system prompts, eventually
   voice). Real AI infra line item + per-user inference cost. This
   is where the moat lives — no other options app has it. Decision
   needed before app v1 architecture is set.
2. **Real-time options data path.** A scanner against live chains
   needs OPRA feed access (direct or via polygon.io / dxFeed /
   Tradier). $thousands/mo at low scale, more at consumer scale.
   At launch (paper-trade only) we can plausibly use 15-min delayed
   data and dodge the licensing cost — decide explicitly.
3. **Phase 2 — real-money execution.** Three real paths (introducing
   broker, BD registration, broker hand-off). See `COMPLIANCE.md`
   §5 for trade-offs. Defer the decision but start the attorney
   conversation early.
4. **Defensible wedge.** Closest comp is Option Alpha (scanner +
   automation + education) — Theta's differentiator over them is
   the bonded coach. Lose the coach and Theta is Option Alpha. Lose
   the ease and it's Tastytrade Lite. Lose the scanner and it's
   Headspace. Wedge = **coach × ease × scanner**; protect all three.
5. **Production scope = venture-scale.** Mobile app team + data
   infra + (eventually) broker integration + coach AI infra +
   compliance + 20-lesson production pipeline. Not a side project.
   Plan the team and the round accordingly.

## 4. Capability / Skill Map (what we actually have)
- **Soul character training** — train each coach once as a reusable
  identity for consistent faces across all videos. Highest priority.
- **Image generation** — characters, key art, marketing stills.
- **Video generation** — lesson videos, coach intros, ads.
- **Storyboard pipeline (free)** — mermaid pitches, zero credits.
- **Design lead (this doc)** — product/marketing/narrative coherence.
- Credit reality: ~44 generation credits = budget-gated. Design is free;
  generation is metered. Storyboard everything before generating anything.

## 5. Next Process (proposed order)
1. Pick fonts (3a) — one message.
2. Get the Lesson 9 reference or set the bar (3d).
3. Storyboard lessons 2–19 (free) to lock the creative spine.
4. Train the 4 coaches as Soul characters (small credit spend, huge reuse).
5. Generate one hero lesson video end-to-end as the quality bar.
6. Shape marketing once the spine is locked.
