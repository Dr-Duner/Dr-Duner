# Theta — Conversation Handoff

Snapshot of this working session so any future chat (or Cowork, or you)
can resume with zero re-explaining. Read `CLAUDE.md` and
`theta/DESIGN.md` first; this file is the "what just happened + what's
next" layer on top of them.

## Where things stand
- This repo (`Dr-Duner`, branch `claude/evaluate-mobile-workflow-nbDLD`)
  is the single source of truth for Theta design work.
- Persistence is now wired: `CLAUDE.md` (auto-loaded every session),
  `theta/DESIGN.md` (living spec), this handoff.

## Done this session
- `theta/lesson-flow.mmd` / `.png` — Theta cast + 20-lesson arc flowchart.
- `theta/lesson1-storyboard.mmd` / `.png` — Lesson 1 video storyboard
  pitch (6 shots, ~35s vertical, Nova lead). No video generated.
- `theta/DESIGN.md` — living design doc (locked vs. open decisions,
  capability map, next-process order).
- `CLAUDE.md` — auto-loaded shared memory + rules (read DESIGN.md first;
  context boundary; persist decisions immediately).
- Captured from user: coach text = monospace terminal font; Lesson 9
  was built in Cowork and seen in the simulator.

## The core problem surfaced
Claude Code cannot see Cowork, the simulator, or any other session — only
this repo. Foundational Theta context was lost because it lived in Cowork,
not here. Fix in place: everything must be written to this repo; CLAUDE.md
makes it auto-load for all future Claude Code sessions in this repo. Limit:
this does NOT bridge to Cowork — both tools must use this same repo.

## Open blockers (need user input)
1. **Where does Cowork save its work?** (same repo / different repo /
   only the simulator) — determines if Lesson 9 is recoverable.
2. **Lesson 9 artifact** — upload a screen recording OR describe its
   animation + automation + how the coach appears. It is the bar for 2–19.
3. **Exact terminal font family** — confirm the name to mark LOCKED.
4. **Credits** — ~44 generation credits, starter plan. 18 lesson videos
   won't fit. Design free; generation metered; storyboard before generating.

## Next steps (proposed order)
1. Answer blocker 1 (Cowork storage location).
2. Get Lesson 9 reference (blocker 2).
3. Confirm terminal font (blocker 3).
4. Storyboard lessons 2–19 (free, no credits) to lock the creative spine.
5. Train the 4 coaches as Soul characters (small spend, reused everywhere).
6. Generate one hero lesson video as the quality bar.
7. Shape marketing once the spine is locked.

## Pointers
- Spec / decisions: `theta/DESIGN.md`
- Shared memory / rules: `CLAUDE.md`
- Cast + arc: `theta/lesson-flow.png`
- Lesson 1 pitch: `theta/lesson1-storyboard.png`
