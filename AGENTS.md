# AGENTS.md — Orientation

Read this before doing anything in this repository, whichever agent you are.

## What this repository is

Deadhang Labor LLC's public marketing website — a static site (HTML/CSS/JS/images) deployed through GitHub Pages and mapped to `deadhanglaborllc.com`.

It is business-facing public content only.

## Governance model

This repository is paired with and governed by `50yearroadmap`'s `companies/deadhang-labor/` folder (`companies/deadhang-labor/14_sops.md` is the operating checklist for the underlying business).

The repository remains intentionally lightweight: it does not need a local ledger or a duplicate full governance package. However, the owner changed the website change-control rule on 2026-09-07 because `main` is accepted production state.

### PR-first change control

For substantive or user-visible website changes, use:

**ORIENT → REFRESH `main` → WORK BRANCH → CHANGE → VALIDATE → PR → REVIEW → MERGE → VERIFY**

Rules:

- Do not make routine website changes directly on `main`.
- `main` is accepted production state.
- Work branches and pull requests are proposed state.
- `.github/workflows/pages.yml` deploys the site after a PR targeting `main` is merged; it no longer deploys on every direct push to `main`.
- Manual workflow dispatch is reserved for an explicit deployment action.
- GitHub branch-protection settings should enforce the same PR-first rule when technically available; the process rule applies even if the repository setting is temporarily absent.

## Orchestrator operating-layer pointer

Every repository-attached session also enters the lightweight top-level operating/continuity contract in `50yearroadmap/AGENT_ORIENTATION.md` and `50yearroadmap/governance/CONTINUITY_CONTRACT.md`.

- Routine deterministic website work stays local.
- Roadmapdev is optional and relevance-triggered for consequential, cross-system, uncertain, conflicting, or explicitly requested analysis; its output is advisory, not write authority.
- Supabase project `Roadmap` is the durable shared memory/evidence/research plane when available.
- A provider without direct Supabase access uses the canonical `50yearroadmap` bridge/read-through continuity path and must not ask the owner for credentials merely to continue.
- This pointer grants no cross-repository writes and does not change this repository's public-only boundary or live-site deployment rules.

## Write access

Write access to this repository's governing folder inside `50yearroadmap` follows `50yearroadmap/governance/WRITE_ACCESS_PROTOCOL.md`.

Write access to this repository itself likewise requires owner authorization. Technical connector access is not authorization.

## Public-data boundary

- Keep this repository public-facing only.
- Do not add contractor tools, private documents, API keys, `.env` files, database dumps, financial records, client records, or PII.
- Future contractor portals or admin dashboards belong in separate private repositories.
- Historical/source ZIPs and other redundant working artifacts may be removed only after the archive gate confirms an immutable object-storage copy, provenance/hash verification, and tested retrieval.
- `ecosystem-archive-control` stores archive policy/manifests, not raw bulk archive packages.

## Hosting boundary

The current repository build/deploy path is GitHub Actions + GitHub Pages with the custom domain in `CNAME`. A separate cPanel or hosting account may exist outside this repo, but it is not an active deployment target here unless the owner explicitly changes that architecture.

## Standing owner preference

Do not use AskUserQuestion or any multiple-choice/decision-card UI here. Converse in plain text. If blocked on a decision only the owner can make, ask directly in a normal chat message.
