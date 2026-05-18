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
1. **Cowork save location** — does Cowork commit to this repo, another
   repo, or only the simulator? Decides if Lesson 9 is recoverable.
2. **Lesson 9 artifact** — upload a screen recording or describe its
   animation + automation + how the coach appears. It is the bar for 2–19.
3. **Exact terminal font name** — decided in Cowork, never written here;
   genuinely uncaptured. Gee must supply it to lock it.
4. **Credits** — ~44 generation credits; 18 lesson videos won't fit.
   Design is free; generation is metered; storyboard before generating.

## 4. Next steps
1. Gee answers blocker 1 (Cowork location).
2. Recover or re-describe Lesson 9 (blocker 2).
3. Gee names the font; lock it in DESIGN.md + CLAUDE.md (blocker 3).
4. Storyboard lessons 2–19 (free) to lock the creative spine.
5. Train the 4 coaches as Soul characters (small spend, reused everywhere).
6. Generate one hero lesson video as the quality bar.
7. Shape marketing once the spine is locked.

## 5. Pointers
- Spec / decisions: `theta/DESIGN.md`
- Shared memory / rules: `CLAUDE.md`, `theta/memory/MEMORY.md`
- Session records: `theta/SESSION-*.md`
- Cast + arc: `theta/lesson-flow.png`
- Lesson 1 pitch: `theta/lesson1-storyboard.png`
