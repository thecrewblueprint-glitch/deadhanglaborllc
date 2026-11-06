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
