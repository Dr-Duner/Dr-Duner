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

## 2. Locked Decisions
- **LOCKED** Brand name: Theta (symbol Θ).
- **LOCKED** Palette: navy `#0b1f3a`, signal green `#00c896`, off-white `#eef6f3`.
- **LOCKED** Four coaches: Nova (Analyst), Rex (Veteran), Finn (Patient
  Teacher), Atlas (Risk Manager). Identities in `lesson-flow.mmd`.
- **LOCKED** Arc: Lesson 1 (Dichotomy of Control) → 2–19 (mindset + craft)
  → first paper trade closes → coach's one line → Lesson 20 scanner unlock.
- **LOCKED** Lesson 1 video concept: see `lesson1-storyboard.png`.

## 3. Open Decisions (need your call)

### 3a. Typography  — DIRECTION SET (confirm exact family)
- **Decided (from Cowork discussion):** the coach text — the messages the
  customer reads after picking their agent — uses a **monospace computer-
  terminal font**. The terminal aesthetic IS the interface voice.
- **Open:** confirm the exact family. Common terminal monospaces:
  *JetBrains Mono*, *IBM Plex Mono*, *SF Mono*, *Menlo*, *Fira Code*,
  *Cascadia Code*. If the simulator used a specific one, name it here and
  mark **LOCKED**.
- Brand/Θ/lesson-title face (separate from coach text) still open if we
  even want a second face — terminal-only is a valid strong choice.

### 3b. The coach interface (post-selection)  — DESIGN NEEDED
After the user picks a coach, the interface IS the coach texting them in
"our font." Open questions: chat-style bubbles vs. full-screen lines?
Typing animation? Coach avatar still vs. short looping video? Voice/audio?

### 3c. Game format  — DESIGN NEEDED
What makes the lessons a "game": progress/XP, streaks, the locked scanner
as the prize, paper-trade scoreboard, the coach's trust meter? To define.

### 3d. Lessons 2–19 treatment  — DESIGN NEEDED
- **Known:** Lesson 9 was built in **Cowork (not Claude Code)** and viewed
  in the **simulator**. It is the quality/animation/automation bar for
  2–19. Claude Code cannot see it — need it brought here: a screen
  recording uploaded, OR a written description of its animation +
  automation + how the coach appears.
- Engaging + interactive + coach-present throughout (supersedes the old
  "coach stays silent 2–19" line in lesson-flow.mmd — confirm).

### 3e. Marketing  — IDEAS PARKED
User has several marketing ideas. Capture them here as raw bullets, shape
into a plan after the product spine is set.
- (add ideas here)

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
