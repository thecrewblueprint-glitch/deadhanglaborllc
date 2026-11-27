# Temporary AWS reference guard — November 6, 2026

Refs [#53](https://github.com/thecrewblueprint-glitch/deadhanglaborllc/issues/53) and [#55](https://github.com/thecrewblueprint-glitch/deadhanglaborllc/issues/55).

**State: pre-migration safeguard, NOT an AWS exit.** The existing [33-URL public-site inventory](AWS_EXIT_STATIC_ASSETS_2026-11-03.json) is the initial explicit allowance for the old CloudFront hostname. No assets were downloaded, copied, hashed, published to a replacement host, or verified available off AWS. AWS account resources, origin and expiry notice remain unverified.

On this PR branch, the website Pages validation job now invokes `.github/scripts/aws_reference_gate.py` and its synthetic offline tests. It scans first-party HTML/CSS/JS, excludes documentation and generated/preview copies, and **rejects any previously unrecorded AWS/CloudFront source URL**. It allows the 33 existing external URLs to remain temporarily so that an unrelated website PR does not break production images. Existing sources can eliminate references as individual replacement images are verified and approved. The scanner does not request network access, AWS permissions, service account credentials, or private assets.

Read-only source comparison of the original 14 audited primary files found no unlisted AWS URL on November 6. This is a connector source comparison, **not** a native GitHub Actions result or live HTTP image test; other site assets and AWS account resources remain outside this bounded comparison.

Commands after checkout:

```sh
python -m unittest discover -s .github/tests -p 'test_*.py' -v
python .github/scripts/aws_reference_gate.py
# Only after authorized, fully verified cutover:
python .github/scripts/aws_reference_gate.py --require-zero
```

**Release rule:** Neither the pre-migration passing gate nor a later `--require-zero` pass proves S3 versions, account ownership, private backups or provider charges were handled. The cutover still requires a per-asset original-byte/hash receipt, owner-approved public destination, website link/broken-image review, rollback plan and independent restore; no AWS service is decommissioned without owner approval.

## R03-B deployment artifact mode (draft)

The existing CLI now offers explicit offline artifact qualification after the existing Pages build. Supply an independently reviewed manifest (JSON array of exact path/SHA-256 objects) and its independently verified file SHA-256; never derive approval from the artifact under test. Example, after a disposable build:

```sh
python .github/scripts/aws_reference_gate.py \\
  --artifact-root _site \\
  --reviewed-manifest /restricted/reviewed-public-files.json \\
  --manifest-sha256 INDEPENDENTLY_REVIEWED_FILE_DIGEST
```

The gate checks the entire artifact inventory before reading file bytes, denies forbidden paths, symlinks, unreviewed types, extra/missing files and hash drift, then checks literal AWS URLs across reviewed text types (including deployed documentation, JSON, webmanifest and SVG). Binary images/fonts are hash-only. Dynamic references and actual CDN/storage remain unverified. Source-only mode is unchanged. New module and 14 tests match the offline qualified files. No workflow activation or deployment change; full existing suite and actual built artifact have not been qualified. The final reviewed public manifest, preview dependency disposition, any explicit packaging exclusions and pre-release workflow enforcement remain required before release; do not auto-approve files or remove public assets to make the gate pass.

## CL03 — public document disposition and conditional release gate

Owner decision: review the four previously identified public website files for privacy; preserve publication if safe. Keep originals and existing deployed state unchanged during review. No blanket exception for credential directories or PDF files.

The audited draft contains four document paths; current main `dcebdefa6780946a11a4bd679cf2ebb028295cd4` adds an updated resume under two filenames (same blob), and changes the credential HTML. Review must use the actual accepted tree rather than the stale draft.

| Document category | Draft blob(s) | Current main blob(s) | Review |
|---|---|---|---|
| Credential HTML | 0a7ce996c61d4faa59270e14eac078b7fb1ecb51 | f3ae455f185cd4380b27cdfe1e1cfafa7b5b4c75 | Source inspected: local-only links, no detected contact/address/form/script or actual card number; current HTML states physical card/number/QR are private. Conditional on linked assets review. |
| Certificate preview image | 02337fbc83bd1a148834d3ddd6fedf669dc72c94 | same | Visually inspected exact returned image; verification QR visible. Do not expose verification token in logs. Separate certificate verification destination and public rights need review. |
| Certificate PDF | f32da37c8569007cc7fb74da1fb21e98db0f25ac | same | Exact blob identified, full PDF render/metadata/hidden content and verification destination review not completed. |
| Resume PDF | 8f7a661e48a624278b0f85f379a89b985836a392 | 38b0ce7bfca8f15ab8e457cf381e237a4517dd86 (two paths) | Exact blobs identified; render, metadata, contact fields and references not reviewed. Review latest version; do not restore old resume or delete duplicate without an explicit release plan. |

Native public-site DNS and PDF retrieval unavailable; public PDF open also unsuccessful. No sensitive values copied into the report, no QR navigation, no certificate/resume content declared safe without full review.

The offline gate now accepts ONLY the five named candidate paths when the independently reviewed digest-pinned manifest includes `publication_review: "privacy_and_publication_verified"` for each exact path/SHA-256. All other credential-directory entries and PDF files remain denied, unmarked candidates denied, HTML still scanned, PDF/JPEG magic and exact hash required. The marker is a reviewer attestation, not automatic approval; actual review must cover visible/hidden content, metadata/attachments, QR destinations, rights and public audience. No real document marked approved. Existing deployment workflow unchanged. Native Python synthetic tests 20/20 pass, exact module/test Git blobs 19a1cf2735aa37426aa7442bebba93e03bf5a9d5 and b65691986b0c66534577dd44e7ab8c759f37cc88. Actual full artifact and independent manifest still pending.

The four image references in the excluded preview page are not evidence of dependencies in the current public artifact; retain preview privately and reconcile actual approved release manifest before changing AWS policy. Public internal documentation exposure remains a separate open review; no files removed or live publication changed.
