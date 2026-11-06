#!/usr/bin/env python3
"""Block NEW AWS URL dependencies while an explicitly unverified migration is pending.

Read-only source gate. This does not access AWS, download media, prove backups,
publish replacement assets, change DNS, or authorize AWS retirement. Known 2026-11-03
CloudFront URLs remain permitted ONLY until verified replacements are installed.
After cutover use --require-zero to forbid all AWS references in first-party site code.
"""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

AWS_URL = re.compile(
    r"(?:(?:https?:)?//)(?:[A-Za-z0-9-]+\.)*(?:cloudfront\.net|amazonaws\.com)(?:/[^\s\"'<>)]*)?",
    re.IGNORECASE,
)
SOURCE_EXTENSIONS = {".html", ".css", ".js"}
EXCLUDED_DIRS = {".git", ".github", "_site", "docs", "preview",
                 "credentials", "node_modules", "__pycache__"}


def scan(root):
    """Return normalized AWS URL -> source paths; ignore docs and generated builds."""
    found = {}
    for file in sorted(root.rglob("*")):
        if not file.is_file() or file.suffix.lower() not in SOURCE_EXTENSIONS:
            continue
        rel = file.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in rel.parts[:-1]):
            continue
        for raw in AWS_URL.findall(file.read_text(encoding="utf-8-sig")):
            normalized = "https:" + raw if raw.startswith("//") else raw
            found.setdefault(normalized, set()).add(rel.as_posix())
    return found


def audit(inventory, observed, require_zero=False):
    if inventory.get("schema_version") != "deadhang-aws-static-asset-inventory/1.0.0":
        raise ValueError("Unrecognized website AWS inventory")
    rows = inventory.get("asset_rows")
    if not isinstance(rows, list) or len(rows) != inventory.get("unique_external_urls"):
        raise ValueError("Baseline inventory missing or internally inconsistent")
    known = [row["url"] for row in rows]
    if len(set(known)) != len(known):
        raise ValueError("Duplicate baseline URL")
    extra = sorted(set(observed) - set(known))
    failures = []
    if extra:
        # Do not expose signed query parameters or credentials in CI logs.
        failures.append("New unapproved AWS URLs: " + str(len(extra)) +
                        "; update inventory through reviewed migration evidence")
    if require_zero and observed:
        failures.append("Cutover gate: " + str(len(observed)) +
                        " AWS URL(s) remain in site sources")
    return {"ok": not failures, "errors": failures,
            "baseline_unique_urls": len(known),
            "remaining_known_urls": len(set(observed) & set(known)),
            "new_aws_url_count": len(extra),
            "sources_with_aws_refs": len({p for refs in observed.values() for p in refs}),
            "zero_aws_refs": not bool(observed)}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    p.add_argument("--require-zero", action="store_true",
                   help="Owner-approved post-cutover gate; NOT expected to pass before migration")
    args = p.parse_args(argv)
    root = args.root.resolve()
    inventory = json.loads((root / "docs/AWS_EXIT_STATIC_ASSETS_2026-11-03.json").read_text(encoding="utf-8"))
    result = audit(inventory, scan(root), args.require_zero)
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
