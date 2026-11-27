import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from aws_artifact_gate import audit_artifact, PUBLIC_DOCUMENTS, REVIEW_MARK

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

    def reviewed_manifest(self):
        return [dict(row,publication_review=REVIEW_MARK) if row['path'] in PUBLIC_DOCUMENTS else row for row in self.manifest()]
    def test_all_named_document_candidates_require_review(self):
        for path,kind in PUBLIC_DOCUMENTS.items():
            self.put(path,{'pdf':b'%PDF-1.4 synthetic only','jpeg':b'\xff\xd8\xffsynthetic','text':b'<p>synthetic</p>'}[kind])
        self.assertRaises(ValueError,self.check)
        result=audit_artifact(self.root,self.reviewed_manifest(),BASE)
        self.assertTrue(result['ok']);self.assertEqual(result['reviewed_public_documents'],5)
        self.assertEqual(result['binary_hash_only'],4)
    def test_document_review_cannot_extend_path_scope(self):
        for path in ['credentials/other.pdf','assets/credentials/other.jpg','assets/other.pdf','Credentials/osha-30.html']:
            with self.subTest(path=path):
                self.put(path,b'%PDF-fixture');m=self.manifest()
                m[0]['publication_review']=REVIEW_MARK
                self.assertRaises(ValueError,audit_artifact,self.root,m,BASE)
                (self.root/path).unlink()
                for parent in (self.root/path).parents:
                    if parent==self.root:break
                    try:parent.rmdir()
                    except OSError:break
    def test_reviewed_document_exact_hash_and_type(self):
        path='credentials/osha-30.pdf';self.put(path,b'%PDF-fixture')
        m=self.reviewed_manifest();self.put(path,b'%PDF-changed')
        self.assertRaises(ValueError,audit_artifact,self.root,m,BASE)
        self.put(path,b'not a pdf');self.assertRaises(ValueError,audit_artifact,self.root,self.reviewed_manifest(),BASE)
    def test_document_marker_does_not_bypass_text_scan(self):
        self.put('credentials/osha-30.html','<img src="https://unreviewed.cloudfront.net/x">')
        self.assertFalse(audit_artifact(self.root,self.reviewed_manifest(),BASE)['ok'])
    def test_unreviewed_neighbor_denied_before_read(self):
        self.put('credentials/osha-30.pdf',b'%PDF-fixture');m=self.reviewed_manifest()
        self.put('credentials/private.txt','SYNTHETIC')
        self.assertRaises(ValueError,audit_artifact,self.root,m,BASE)
    def test_unrecognized_review_attestation_denied(self):
        self.put('credentials/osha-30.pdf',b'%PDF-fixture');m=self.manifest()
        m[0]['publication_review']='pending'
        self.assertRaises(ValueError,audit_artifact,self.root,m,BASE)

if __name__=='__main__':unittest.main()
