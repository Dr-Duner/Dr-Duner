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

RESOLVED (Kevin approved, option A): `main` is the blind-clone safety
mirror. Every backup/handoff: push the working branch, then
`git checkout main && git merge --ff-only <branch> && git push origin main`
and return to the working branch. Any fresh clone — any branch — now has
the full knowledge layer. Work still happens on
`claude/evaluate-mobile-workflow-nbDLD`.
