# Deadhang website AWS exit — source-reference inventory

**Snapshot:** 2026-11-03 · GitHub website main `35bd95f9404ffecae4024f9438579ebfd20c7f67` · source-based audit only.

Scanned **14** primary HTML/CSS/JS sources. **5** contain AWS CloudFront asset URLs; **33 unique externally hosted image URLs** were found. Exact filename lookups for these URLs in the repository's `images/` directory found **0 matches**. This does not prove the existing local photos are equivalent or that the remote images are recoverable.

**Critical qualification:** No AWS-account inventory, origin/bucket access, object downloads, checksums, versions, policy audit, or non-website AWS resource sweep was completed. The separate complete AWS exit issue [#53](https://github.com/thecrewblueprint-glitch/deadhanglaborllc/issues/53) remains open. The tool environment could not retrieve the CDN image bytes. Do not claim a backup or migration from this report.

## Where the live HTML depends on CloudFront

| Source page | Unique CloudFront URLs |
|---|---:|
| `index.html` | 2 |
| `about.html` | 2 |
| `portfolio.html` | 31 |
| `services.html` | 1 |
| `contact.html` | 1 |

## Exact public-site asset references

| Remote filename | Referenced in | Matching local file by exact name |
|---|---|---|
| [about-teaser.jpg](https://djrzj431udyjd.cloudfront.net/about-teaser.jpg) | `about.html` | Not found |
| [arena-1.jpg](https://djrzj431udyjd.cloudfront.net/arena-1.jpg) | `portfolio.html`, `contact.html` | Not found |
| [arena-2.jpg](https://djrzj431udyjd.cloudfront.net/arena-2.jpg) | `portfolio.html` | Not found |
| [arena-3.jpg](https://djrzj431udyjd.cloudfront.net/arena-3.jpg) | `portfolio.html` | Not found |
| [arena-4.jpg](https://djrzj431udyjd.cloudfront.net/arena-4.jpg) | `portfolio.html` | Not found |
| [arena-5.jpg](https://djrzj431udyjd.cloudfront.net/arena-5.jpg) | `portfolio.html`, `services.html` | Not found |
| [arena-6.jpg](https://djrzj431udyjd.cloudfront.net/arena-6.jpg) | `portfolio.html` | Not found |
| [arena-7.jpg](https://djrzj431udyjd.cloudfront.net/arena-7.jpg) | `portfolio.html` | Not found |
| [arena-8.jpg](https://djrzj431udyjd.cloudfront.net/arena-8.jpg) | `portfolio.html` | Not found |
| [arena-9.jpg](https://djrzj431udyjd.cloudfront.net/arena-9.jpg) | `portfolio.html` | Not found |
| [country-thunder-wisconsin-1.jpg](https://djrzj431udyjd.cloudfront.net/country-thunder-wisconsin-1.jpg) | `portfolio.html` | Not found |
| [country-thunder-wisconsin-2.jpg](https://djrzj431udyjd.cloudfront.net/country-thunder-wisconsin-2.jpg) | `portfolio.html` | Not found |
| [country-thunder-wisconsin-3.jpg](https://djrzj431udyjd.cloudfront.net/country-thunder-wisconsin-3.jpg) | `portfolio.html` | Not found |
| [country-thunder-wisconsin-4.jpg](https://djrzj431udyjd.cloudfront.net/country-thunder-wisconsin-4.jpg) | `portfolio.html` | Not found |
| [country-thunder-wisconsin-5.jpg](https://djrzj431udyjd.cloudfront.net/country-thunder-wisconsin-5.jpg) | `portfolio.html` | Not found |
| [festival-1.jpg](https://djrzj431udyjd.cloudfront.net/festival-1.jpg) | `portfolio.html` | Not found |
| [festival-10.jpg](https://djrzj431udyjd.cloudfront.net/festival-10.jpg) | `portfolio.html` | Not found |
| [festival-11.jpg](https://djrzj431udyjd.cloudfront.net/festival-11.jpg) | `portfolio.html` | Not found |
| [festival-12.jpg](https://djrzj431udyjd.cloudfront.net/festival-12.jpg) | `portfolio.html` | Not found |
| [festival-2.jpg](https://djrzj431udyjd.cloudfront.net/festival-2.jpg) | `portfolio.html` | Not found |
| [festival-3.jpg](https://djrzj431udyjd.cloudfront.net/festival-3.jpg) | `about.html`, `portfolio.html` | Not found |
| [festival-4.jpg](https://djrzj431udyjd.cloudfront.net/festival-4.jpg) | `portfolio.html` | Not found |
| [festival-5.jpg](https://djrzj431udyjd.cloudfront.net/festival-5.jpg) | `portfolio.html` | Not found |
| [festival-7.jpg](https://djrzj431udyjd.cloudfront.net/festival-7.jpg) | `portfolio.html` | Not found |
| [festival-8.jpg](https://djrzj431udyjd.cloudfront.net/festival-8.jpg) | `portfolio.html` | Not found |
| [festival-9.jpg](https://djrzj431udyjd.cloudfront.net/festival-9.jpg) | `portfolio.html` | Not found |
| [headshot.jpg](https://djrzj431udyjd.cloudfront.net/headshot.jpg) | `portfolio.html` | Not found |
| [hero-bg.jpg](https://djrzj431udyjd.cloudfront.net/hero-bg.jpg) | `index.html` | Not found |
| [portfolio-1.jpg](https://djrzj431udyjd.cloudfront.net/portfolio-1.jpg) | `portfolio.html` | Not found |
| [spotlight-1.jpg](https://djrzj431udyjd.cloudfront.net/spotlight-1.jpg) | `portfolio.html` | Not found |
| [spotlight-4.jpg](https://djrzj431udyjd.cloudfront.net/spotlight-4.jpg) | `portfolio.html` | Not found |
| [spotlight-5.jpg](https://djrzj431udyjd.cloudfront.net/spotlight-5.jpg) | `portfolio.html` | Not found |
| [spotlight-6.jpg](https://djrzj431udyjd.cloudfront.net/spotlight-6.jpg) | `index.html`, `portfolio.html` | Not found |

## Safe completion sequence

1. Verify the AWS account ownership and the actual expiry/deletion notice. Inventory S3 objects/versions, CloudFront origin, other Deadhang AWS services and non-public dependencies independently. Preserve AWS source access until full recovery.
2. Obtain an approved, portable, non-AWS backup of each exact image. Record byte count, file type, source identifier and SHA-256. Verify retrieval and any required usage rights. No substitution based only on a filename.
3. Place verified public assets in the approved static-site destination, keeping private assets out of public GitHub. Record source URL → destination relative path map.
4. Update HTML/CSS on a work branch, run local link checks, review preview and obtain owner approval before production cutover. Keep original CDN references in a reversible log.
5. Confirm every live image loads in multiple browsers and that the old CDN is no longer referenced. Verify non-website assets and restorability separately; decommission AWS only after explicit authorization and full dependency check.

## Boundaries

- This is a **non-destructive inventory commit**. No website image URLs, deployment, DNS or AWS service settings are modified.
- The listed public image URLs are existing source dependencies; their presence is not proof of bucket contents or asset ownership.
- Website owner review tracked separately in [#55](https://github.com/thecrewblueprint-glitch/deadhanglaborllc/issues/55).

Machine-readable list: [AWS_EXIT_STATIC_ASSETS_2026-11-03.json](AWS_EXIT_STATIC_ASSETS_2026-11-03.json).
