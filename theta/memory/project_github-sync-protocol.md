# project_ GitHub sync protocol (Kevin-confirmed)

Decision: GitHub is the single sync backbone across all environments.

- **Session start:** the cloud container auto-clones the repo from
  GitHub. Knowledge is "uploaded" automatically at start. CLAUDE.md
  auto-loads and points to HANDOFF.md + DESIGN.md + this memory index.
- **"Back it up" / "create a handoff" / end of session:** commit + push
  EVERYTHING to GitHub. Push = next session downloads it on clone.
- **Banned transfer channels:** Gmail drafts, pastebin, Telegram. Git
  only. Local ~/.claude does not cross machines — never rely on it.

## Single point of failure — BRANCH
A fresh session clones ONE branch. All Theta work lives on
`claude/evaluate-mobile-workflow-nbDLD`. `main` has only README.md.
A session starting on `main` would be blind.

Rule until resolved: every Theta session MUST run on
`claude/evaluate-mobile-workflow-nbDLD`. Open decision: mirror canonical
docs to `main` as a safety net (needs Kevin's yes — pushing to main).
