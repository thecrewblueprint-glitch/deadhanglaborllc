# CLAUDE.md — Session Preferences

## Read AGENTS.md first

This repository's orientation lives in `AGENTS.md` at the repository root — read it before doing anything else here. It covers what this repository is, its governance boundary with `50yearroadmap`, PR-first change control, write access, deployment behavior, and content boundaries.

## Never use AskUserQuestion (or any multiple-choice/decision-card UI)

The owner's standing preference applies here too: converse in plain text only. If blocked on a decision only the owner can make, ask directly in a normal chat message — don't render it as a card with selectable options.

## Paired with 50yearroadmap

This repo (the public Deadhang Labor LLC marketing site) is governed by `50yearroadmap`'s `companies/deadhang-labor/` folder. Every session should have both repos attached. If this is a fresh session: read `50yearroadmap/AGENT_ORIENTATION.md` first, then `AGENTS.md` in this repo, then `companies/deadhang-labor/14_sops.md` for the operating checklist.

Write access and cross-repository switching follow `50yearroadmap/governance/WRITE_ACCESS_PROTOCOL.md`.

## Governance path: lightweight + PR-first

The 2026-08-24 review correctly concluded that this website does not need a duplicate full local governance package, ledger, or heavy multi-agent process.

The owner revised the change-control portion on 2026-09-07: because `main` is production state, routine and substantive website changes now use a work branch and pull request before merge. See `AGENTS.md` for the controlling local rule.

The Pages workflow deploys accepted `main` after a PR is merged, rather than deploying every direct push to `main`.
