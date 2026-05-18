# Theta — Handoff

For Gee. Read `CLAUDE.md` + `theta/DESIGN.md` + `theta/memory/MEMORY.md`
first; this is the "where we are / what's next" layer.

## 1. State
Persistence is solved. The repo is the single source of truth across all
Claude Code sessions. Gee can open a fresh session, say "continue Theta,"
and it is briefed automatically — he does not re-explain anything.

## 2. Done this session
- `CLAUDE.md` — auto-loads every session; rules + foundational facts.
- `theta/DESIGN.md` — living spec (locked vs. open decisions).
- `theta/memory/` — MEMORY.md index + project_ decision files.
- `main` made the blind-clone safety mirror; synced every backup.
- `.claude/settings.json` — Stop hook auto-commits + pushes every
  session so nothing is ever lost (active for all future sessions).
- Captured: coach text = monospace terminal font (exact family still
  unconfirmed); Lesson 9 built in Cowork, seen in simulator.

## 3. Open blockers (need Gee)
1. **Lesson 9 artifact** — the real L9 (built in Cowork, seen in
   simulator) is the animation/automation bar. Provisional L9 is in
   place so the arc holds; swap when Gee surfaces it (recording or
   written description).
2. **Credits** — ~44 generation credits; 18 lesson videos won't fit.
   Design is free; generation is metered; storyboard before generating.
- Font: LOCKED (IBM Plex Mono). Persistence: SOLVED.

## 4. Next steps
0. VISION locked + scope locked (universal spine for ALL 19 lessons +
   marketing; "ancient and modern at once"). Production storyboards
   rendered: `storyboard-production-template.png` (the video shot-by-
   shot + App-Store quality bar), `storyboard-frame-layout.png` (9:16
   grid, also the in-app coach-UI language), `storyboard-L5-theta.png`.
   All 19 in `LESSONS.md` re-cut onto the template + per-lesson SCAN
   card. Open: Finn/Atlas everyday scenes (TBD — Gee defines).
1. Gee reviews the production storyboards; lock/adjust the quality bar.
2. Render remaining per-lesson middles L5-style on request.
3. Swap provisional L9 when the Cowork original surfaces.
4. Train the 4 coaches as Soul characters (small spend, reused everywhere).
5. Generate one hero lesson video as the quality bar.
6. Shape marketing once the spine is locked.

## 5. Pointers
- Spec / decisions: `theta/DESIGN.md`
- Shared memory / rules: `CLAUDE.md`, `theta/memory/MEMORY.md`
- Session records: `theta/SESSION-*.md`
- Cast + arc: `theta/lesson-flow.png`
- Lesson 1 pitch: `theta/lesson1-storyboard.png`
