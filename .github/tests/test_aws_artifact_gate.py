import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from aws_artifact_gate import audit_artifact

KNOWN='https://fixture.cloudfront.net/a.jpg'
BASE={'schema_version':'deadhang-aws-static-asset-inventory/1.0.0','unique_external_urls':1,'asset_rows':[{'url':KNOWN}]}
class ArtifactTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
    def put(self,path,text):
        p=self.root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(text.encode() if isinstance(text,str) else text)
    def manifest(self):
        return [{'path':p.relative_to(self.root).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(self.root.rglob('*')) if p.is_file()]
    def check(self,**kw):return audit_artifact(self.root,self.manifest(),BASE,**kw)
    def test_legacy_and_zero(self):
        self.put('index.html',f'<img src={KNOWN}>');self.assertTrue(self.check()['ok']);self.assertFalse(self.check(require_zero=True)['ok'])
    def test_removed(self):
        self.put('index.html','<img src="local.jpg">');self.assertTrue(self.check(require_zero=True)['ok'])
    def test_docs_and_json_deployed(self):
        self.put('docs/public.md','https://unreviewed.cloudfront.net/x');self.put('manifest.webmanifest',json.dumps({'icons':[{'src':'https://fixture.amazonaws.com/y'}]}));self.assertEqual(self.check()['unapproved_urls'],2)
    def test_protocol_relative_svg_srcset(self):
        self.put('index.html','<img srcset="//fixture.cloudfront.net/a.jpg 1x, //new.cloudfront.net/b.jpg 2x">');self.put('icon.svg','<image href="//third.cloudfront.net/c.jpg"/>');self.assertEqual(self.check()['unapproved_urls'],2)
    def test_escaped_json(self):
        self.put('site.json',r'{"src":"https:\/\/new.cloudfront.net\/a.jpg"}');self.assertEqual(self.check()['unapproved_urls'],1)
    def test_binary_hash_only(self):
        self.put('img/a.png',b'\x89PNG\r\nfixture');self.assertEqual(self.check()['binary_hash_only'],1)
    def test_manifest_missing_file(self):
        self.put('index.html','fixture');m=self.manifest();self.put('extra.js','fixture');self.assertRaises(ValueError,audit_artifact,self.root,m,BASE)
    def test_manifest_digest_drift(self):
        self.put('index.html','fixture');m=self.manifest();self.put('index.html','changed');self.assertRaises(ValueError,audit_artifact,self.root,m,BASE)
    def test_private_path_denied(self):
        self.put('credentials/private.txt','SYNTHETIC');self.assertRaises(ValueError,self.check)
    def test_preview_denied(self):
        self.put('preview/index.html','fixture');self.assertRaises(ValueError,self.check)
    def test_unknown_type_denied(self):
        self.put('fixture.bin',b'synthetic');self.assertRaises(ValueError,self.check)
    def test_symlink_denied(self):
        self.put('index.html','fixture');m=self.manifest();(self.root/'alias.html').symlink_to(self.root/'index.html');self.assertRaises(ValueError,audit_artifact,self.root,m,BASE)
    def test_case_collision_denied(self):
        self.put('index.html','fixture');self.put('INDEX.html','fixture');self.assertRaises(ValueError,self.check)
    def test_log_sanitization(self):
        self.put('index.html','https://unreviewed.cloudfront.net/a?token=SYNTHETIC');r=self.check();self.assertFalse(r['ok']);self.assertNotIn('SYNTHETIC',json.dumps(r));self.assertNotIn('unreviewed.cloudfront.net',json.dumps(r))

if __name__=='__main__':unittest.main()
