"""Synthetic and source-reference tests for non-destructive AWS exit guard."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from aws_reference_gate import audit, scan


def baseline():
    return {"schema_version": "deadhang-aws-static-asset-inventory/1.0.0",
            "unique_external_urls": 1,
            "asset_rows": [{"url": "https://d111.cloudfront.net/example.jpg"}]}


class WebsiteAwsGate(unittest.TestCase):
    def test_legacy_references_can_remain_until_verified_cutover(self):
        observed = {"https://d111.cloudfront.net/example.jpg": {"index.html"}}
        self.assertTrue(audit(baseline(), observed)["ok"])
        self.assertFalse(audit(baseline(), observed, require_zero=True)["ok"])

    def test_replacement_can_remove_known_urls(self):
        result = audit(baseline(), {}, require_zero=True)
        self.assertTrue(result["ok"])
        self.assertEqual(result["remaining_known_urls"], 0)

    def test_unapproved_new_host_is_blocked_without_logging_urls(self):
        observed = {"https://private.s3.us-east-1.amazonaws.com/object?token=SECRET": {"index.html"}}
        result = audit(baseline(), observed)
        self.assertFalse(result["ok"])
        self.assertEqual(result["new_aws_url_count"], 1)
        self.assertNotIn("SECRET", json.dumps(result))
        self.assertNotIn("private.s3", json.dumps(result))

    def test_source_scan_detects_new_cloudfront_and_s3_without_scanning_docs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "index.html").write_text('<img src="https://d111.cloudfront.net/example.jpg">')
            (root / "css").mkdir()
            (root / "css/style.css").write_text('body{background:url(//d222.cloudfront.net/hero.jpg)}')
            (root / "docs").mkdir()
            (root / "docs/old.html").write_text('<img src="https://d333.cloudfront.net/old.jpg">')
            found = scan(root)
            self.assertEqual(set(found), {
                "https://d111.cloudfront.net/example.jpg",
                "https://d222.cloudfront.net/hero.jpg",
            })
            self.assertEqual(found["https://d111.cloudfront.net/example.jpg"], {"index.html"})

    def test_baseline_integrity_is_not_silently_ignored(self):
        b = baseline()
        b["unique_external_urls"] = 99
        with self.assertRaisesRegex(ValueError, "inconsistent"):
            audit(b, {})


if __name__ == "__main__":
    unittest.main()
