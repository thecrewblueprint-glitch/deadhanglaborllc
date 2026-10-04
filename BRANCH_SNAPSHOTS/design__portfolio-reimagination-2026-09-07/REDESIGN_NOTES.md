# Deadhang Labor LLC — Portfolio Reimagination

**Status:** experimental / review branch only  
**Created:** 2026-09-07  
**Accepted production branch:** `main`  
**Pre-redesign snapshot:** `snapshot/pre-redesign-2026-09-07` at `c7f5f9e222933fa0ed95d48a5f4591b2468fe961`  
**Redesign branch:** `design/portfolio-reimagination-2026-09-07`

## Safety / rollback

This redesign does not modify accepted production state until a future owner-approved PR is merged into `main`.

The exact prior site is preserved independently on `snapshot/pre-redesign-2026-09-07`. If the redesign is ever merged and later needs to be reverted, restore the snapshot state through a new governed branch/PR rather than reconstructing the old design manually.

## Design thesis

The redesign intentionally avoids the prior reusable-dashboard/card language. It treats Deadhang Labor LLC as a production field credential rather than a generic service-company template.

Key choices:

- keep the dark gunmetal / royal-plum identity;
- replace the prior Barlow-heavy component system with Archivo + IBM Plex Mono;
- use hard rules, editorial grids, oversized typography, and production-document language;
- prioritize real field photography over decorative UI;
- present the portfolio as numbered production plates and a field log;
- present services as a scope-of-work ledger rather than cards;
- present contact as a production intake sheet;
- keep claims bounded to documented labor/support roles.

## Files in the experimental visual system

- `css/fieldbook.css`
- `js/fieldbook.js`
- `index.html`
- `about.html`
- `portfolio.html`
- `services.html`
- `contact.html`
- `404.html`

The legal documents (`privacy.html`, `cookies.html`, `terms.html`) retain their production text/layout during this visual exploration so the redesign does not casually alter legal wording. If the owner accepts the new visual system, those pages can receive a separate presentation-only pass that preserves their text exactly.

## Deployment boundary

Do not manually dispatch the Pages workflow for this branch. The redesign is proposed state only. Normal Pages deployment remains tied to an owner-approved PR merged into `main`.
