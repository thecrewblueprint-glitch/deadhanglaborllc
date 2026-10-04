# Comprehensive Branch Archive

Created: 2026-10-03

This branch consolidates the pre-pruning branch state of `thecrewblueprint-glitch/deadhanglaborllc`.

- `main` remains the production branch.
- `backup/production` is an exact production backup at archive time.
- `archive/comprehensive` stores browseable snapshots of every branch listed below.
- Snapshot directories use `__` in place of `/` from the original branch name.
- The archive commit also records the unique branch-tip commits as parents so their Git histories remain reachable after old refs are removed.

| Original branch | Tip commit | Snapshot directory |
|---|---|---|
| `audit/deadhang-repo-cleanup-2026-09-07` | `8e5fde11d781c490d1125529dad777c1b62d472c` | `BRANCH_SNAPSHOTS/audit__deadhang-repo-cleanup-2026-09-07` |
| `backup/production` | `a6f822b867f702d3dcbd6647b6c876b31c13fe1d` | `BRANCH_SNAPSHOTS/backup__production` |
| `chore/pages-source-redesign-2026-09-07` | `cca51dddd27b4325ba4072903e2780e9b49a6053` | `BRANCH_SNAPSHOTS/chore__pages-source-redesign-2026-09-07` |
| `chore/remove-migrated-image-binaries-2026-09-07` | `885a5199e1ef5043d46709db0209cf26f70fb5b1` | `BRANCH_SNAPSHOTS/chore__remove-migrated-image-binaries-2026-09-07` |
| `chore/s3-image-cutover-2026-09-07` | `617378394c5ef73f9fe68566d4df3bc89679fe82` | `BRANCH_SNAPSHOTS/chore__s3-image-cutover-2026-09-07` |
| `claude/deadhang-labor-fixes-044g4q` | `c4b4171cd86e417f03c87f47b8799995fb61a9cb` | `BRANCH_SNAPSHOTS/claude__deadhang-labor-fixes-044g4q` |
| `claude/deadhang-labor-website-review-w0kn1q` | `ef321c32b0479276566c5c5cddc1803a74495871` | `BRANCH_SNAPSHOTS/claude__deadhang-labor-website-review-w0kn1q` |
| `claude/github-pages-audit-dyyfmj` | `1cc5cc65afe86311d83fd7163e0ab9621b2e67f5` | `BRANCH_SNAPSHOTS/claude__github-pages-audit-dyyfmj` |
| `claude/new-session-qy2zod` | `12163e4224cf76644264a1c0df348834a8eec8bd` | `BRANCH_SNAPSHOTS/claude__new-session-qy2zod` |
| `claude/repository-connections-h5mf2e` | `d5e8f6621935dd94e8bcda8f448552fd49c5b6a6` | `BRANCH_SNAPSHOTS/claude__repository-connections-h5mf2e` |
| `concept/company-rethink-2026-09-07` | `19515b5cd9f654324423fa7223b3aa5931ea96ad` | `BRANCH_SNAPSHOTS/concept__company-rethink-2026-09-07` |
| `concept/credential-rethink-2026-09-07` | `6e39be6215d36a8a91bed690e24bc4e28c9c3c0a` | `BRANCH_SNAPSHOTS/concept__credential-rethink-2026-09-07` |
| `concept/hybrid-rethink-2026-09-07` | `8b510358d7f08fa66ee0dfc2521436d7659d80ba` | `BRANCH_SNAPSHOTS/concept__hybrid-rethink-2026-09-07` |
| `design/portfolio-reimagination-2026-09-07` | `2b83ff2c654e367be9aae2baeb0255cb836f9280` | `BRANCH_SNAPSHOTS/design__portfolio-reimagination-2026-09-07` |
| `dev` | `b84571f05d06680ed2d8048627961a943c33d743` | `BRANCH_SNAPSHOTS/dev` |
| `fix/cookie-banner-storage-wording-2026-10-03` | `576bd6596dde4364bf623ae41bf6357569d77aa1` | `BRANCH_SNAPSHOTS/fix__cookie-banner-storage-wording-2026-10-03` |
| `fix/pages-pr-merge-context-2026-09-07` | `93f5071ffdfcd94766e5644a75bcea1d85f4d950` | `BRANCH_SNAPSHOTS/fix__pages-pr-merge-context-2026-09-07` |
| `fix/pages-redesign-final-artifact-2026-09-07` | `abbb3c4819274a2da0d0d85fdde09abcf78c7fad` | `BRANCH_SNAPSHOTS/fix__pages-redesign-final-artifact-2026-09-07` |
| `fix/tone-down-hero-purple` | `95c5602a3b2b0afe2497863fab443ea5facd0dc5` | `BRANCH_SNAPSHOTS/fix__tone-down-hero-purple` |
| `legal-sync-2026-10-03` | `6abec62c7ef39b5357efd974e0712381b94b10cd` | `BRANCH_SNAPSHOTS/legal-sync-2026-10-03` |
| `main` | `a6f822b867f702d3dcbd6647b6c876b31c13fe1d` | `BRANCH_SNAPSHOTS/main` |
| `perf-indexing-cleanup-2026-10-03` | `71fbb3cbde821b1d096fb97b835fdca731c8c37d` | `BRANCH_SNAPSHOTS/perf-indexing-cleanup-2026-10-03` |
| `production-hardening-2026-10-03` | `f1c1ebab668cacbc119e8cb386184636085aca9c` | `BRANCH_SNAPSHOTS/production-hardening-2026-10-03` |
| `redesign/purple-amber-industrial-2026-09-07` | `e8373e87b670e667c16722d0a66fb23c634c330f` | `BRANCH_SNAPSHOTS/redesign__purple-amber-industrial-2026-09-07` |
| `resume/website-travel-2026-09-25` | `3bbf36fcc2ccc746d2edc7fa60a77a80c36e2a8f` | `BRANCH_SNAPSHOTS/resume__website-travel-2026-09-25` |
| `rollback/pre-redesign-site-2026-09-07` | `fae77c502c260b1b44acef9992ca5f99e1c41543` | `BRANCH_SNAPSHOTS/rollback__pre-redesign-site-2026-09-07` |
| `rollback/restore-pre-redesign-v2-again-2026-09-07` | `f8dc9165900cb4574d63d53806a8118075a222b0` | `BRANCH_SNAPSHOTS/rollback__restore-pre-redesign-v2-again-2026-09-07` |
| `safety/pre-main-redesign-direct-2026-09-07` | `5ea41f16c2fd81ef2a78b288253732f5b53897b6` | `BRANCH_SNAPSHOTS/safety__pre-main-redesign-direct-2026-09-07` |
| `snapshot/pre-purple-amber-redesign-2026-09-07` | `09b43b4ee39d843f28786fbdb5a3f92641c92f46` | `BRANCH_SNAPSHOTS/snapshot__pre-purple-amber-redesign-2026-09-07` |
| `snapshot/pre-redesign-2026-09-07` | `c7f5f9e222933fa0ed95d48a5f4591b2468fe961` | `BRANCH_SNAPSHOTS/snapshot__pre-redesign-2026-09-07` |
| `snapshot/pre-redesign-v2-2026-09-07` | `9023e4ed4d8a11d760047df4efc8fdf17ccee46f` | `BRANCH_SNAPSHOTS/snapshot__pre-redesign-v2-2026-09-07` |
