# Deadhang Labor LLC Website

Static public portfolio website for Deadhang Labor LLC.

**Primary site:** https://deadhanglaborllc.com/

**GitHub Pages project URL:** https://thecrewblueprint-glitch.github.io/deadhanglaborllc/

## Copyright

© 2026 Deadhang Labor LLC. All Rights Reserved.

The source code, branding, graphics, images, documentation, and website content in this repository are proprietary and may not be copied, redistributed, modified, or reused without prior written permission from Deadhang Labor LLC.

## Deployment

This repository uses GitHub Actions + GitHub Pages as the deployment path for the public static site.

- Accepted production state is `main`.
- Website changes are **PR-first**: work branch → pull request → merge to `main`.
- `.github/workflows/pages.yml` deploys only after a pull request targeting `main` is merged, or through an explicit manual workflow dispatch.
- `CNAME` maps the Pages site to `deadhanglaborllc.com`.
- GitHub Pages is currently retained because it provides the HTTPS deployment path used by the custom domain.
- Any separate cPanel/hosting account is outside this repository's current build/deploy authority unless explicitly reactivated as the production target later.

## Repository Structure

```text
/
├── index.html
├── about.html
├── portfolio.html
├── services.html
├── contact.html
├── privacy.html
├── cookies.html
├── terms.html
├── 404.html
├── css/
│   └── style.css
├── js/
│   └── main.js
├── images/
├── favicon.svg
├── site.webmanifest
├── robots.txt
├── sitemap.xml
├── CNAME
├── .nojekyll
└── .github/workflows/pages.yml
```

## Repository hygiene

This is a public website repository, not the business records repository.

- Do not add contractor tools, uploads, private documents, API keys, `.env` files, database dumps, financial records, client records, or PII.
- Historical/source ZIPs and redundant working assets should be removed only after the ecosystem archive gate confirms an immutable object-storage copy, provenance/hash verification, and a tested retrieval path.
- The private `ecosystem-archive-control` repository stores archive manifests/policy only; raw archive packages belong in object storage, not another Git repository.
- Use relative links for internal pages and assets where possible.

## Governance

Any AI agent working in this repository must read `AGENTS.md` first.

This repository is governed by `50yearroadmap`'s `companies/deadhang-labor/` folder. The repository remains lightweight, but the owner adopted PR-first website change control on 2026-09-07 because `main` is production state.
