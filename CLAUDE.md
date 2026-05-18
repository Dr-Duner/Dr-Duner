# CLAUDE.md — Read this first, every session

This file is auto-loaded at the start of every Claude Code session in this
repo. It is the shared memory across all Claude Code chats here.

## RULE 0 — Source of truth (session-start load order)
At session start, before anything: read `theta/HANDOFF.md`,
`theta/DESIGN.md`, and `theta/memory/MEMORY.md` (+ the files it indexes).
These are the living spec. If a fact isn't in this repo, you do not know
it — ask, don't guess. A decision is not real until it is a line here.

## RULE 0b — GitHub sync loop
Session start = repo auto-cloned from GitHub (knowledge arrives
automatically). "Back it up" / "create a handoff" / end of session =
commit + push EVERYTHING to GitHub so the next session clones it. Git is
the only transfer channel. Every Theta session MUST run on branch
`claude/evaluate-mobile-workflow-nbDLD` (main has no Theta work).

## RULE 1 — Context boundary (state this if the user expects lost context)
Claude Code has NO access to Cowork, the simulator, voice chats, or any
other Claude session/product. It only sees this git repo. Lesson 9 and
other work built in Cowork are invisible here unless brought into the repo.

## RULE 2 — Persist immediately
When the user makes a decision, write it into `theta/DESIGN.md` and commit
in the same turn. Never let a decision live only in chat.

## Foundational facts (Theta) — keep current
- Theta: Stoic discipline applied to live options markets. Symbol Θ.
- Product = the coaches' videos + characters + real-time data in a game
  format. The coach is the emotional spine.
- Four coaches: Nova (Analyst), Rex (Veteran), Finn (Patient Teacher),
  Atlas (Risk Manager). Detail in `theta/lesson-flow.mmd`.
- Palette: navy #0b1f3a, signal green #00c896, off-white #eef6f3.
- Coach-facing text uses a monospace computer-terminal font (decided in
  Cowork; exact family TBD — see DESIGN.md 3a).
- Lesson 9 was built in Cowork, viewed in the simulator; it is the bar for
  redoing lessons 2–19. Claude Code cannot see it — must be brought here.
- Arc: L1 Dichotomy of Control → 2–19 mindset+craft → first paper trade →
  coach's one line → L20 scanner unlock → coach goes live.

## Working agreement
- Stable branch for Theta design work: `claude/evaluate-mobile-workflow-nbDLD`
  (keep using the same branch so sessions don't diverge).
- Design/storyboards = free (mermaid, no credits). Video/image generation
  = metered (~44 credits, starter plan). Storyboard before generating.
- Commit + push at every stopping point (container is ephemeral).
