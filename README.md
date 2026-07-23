# Deadhang Labor LLC Website

Static portfolio website for Deadhang Labor LLC, built for GitHub Pages deployment.

## Copyright

© 2026 Deadhang Labor LLC. All Rights Reserved.

The source code, branding, graphics, images, documentation, and website content in this repository are proprietary and may not be copied, redistributed, modified, or reused without prior written permission from Deadhang Labor LLC.

## Deployment

This repository deploys from the `main` branch using GitHub Actions and GitHub Pages.

Required Pages settings:

1. Go to **Settings → Pages**.
2. Set **Source** to **GitHub Actions**.
3. Confirm the custom domain is `deadhanglaborllc.com`.
4. Enable **Enforce HTTPS** after DNS and certificate validation complete.

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

## Notes

- Keep this repository public-facing only.
- Do not add contractor tools, uploads, private documents, API keys, `.env` files, database dumps, or client records here.
- Future contractor portals or admin dashboards should live in separate private repositories.
- Use relative links for internal pages and assets where possible.