# AGENTS.md — Orientation

Read this before doing anything in this repository, whichever agent you are.

## What this repository is

Deadhang Labor LLC's public marketing website — a static site (HTML/CSS/JS/
images) deployed via GitHub Pages. It is business-facing content only.

## Governance model

This repository is paired with and governed by `50yearroadmap`'s
`companies/deadhang-labor/` folder (`companies/deadhang-labor/14_sops.md`
is the operating checklist for the underlying business).

`50yearroadmap`'s governance audited this repository (2026-08-24) and
confirmed a full local governance package (PR-first change control,
ledger model, multi-agent coordination doc, and similar) is not
warranted here: the deploy workflow is minimal and first-party-only, and
no financial/contractor/private data lives in this repository. See
`50yearroadmap`'s `governance/GOVERNANCE_ROLLOUT_TODO.md` for that
record.

That exemption is about process weight, not about skipping orientation —
read this file before making any change, and don't bypass it just
because the repository is small.

## Write access

Write access to this repository's governing folder inside
`50yearroadmap` requires an explicit owner ask and grant, every session —
see `50yearroadmap`'s `governance/WRITE_ACCESS_PROTOCOL.md`. Write access
to this repository itself likewise requires explicit owner
authorization.

## Boundaries

- Keep this repository public-facing only.
- Do not add contractor tools, uploads, private documents, API keys,
  `.env` files, database dumps, or client records here — see
  `README.md`'s Notes section.
- Future contractor portals or admin dashboards belong in separate
  private repositories, not here.
- This repository deploys automatically from `main` via
  `.github/workflows/pages.yml` on every push — a push to `main` is a
  live-site action, not a no-op.

## Standing owner preference

Do not use AskUserQuestion or any multiple-choice/decision-card UI here.
Converse in plain text. If blocked on a decision only the owner can make,
ask directly in a normal chat message.
