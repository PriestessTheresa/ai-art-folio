"""Check a repository staging directory for publishable hygiene."""
from pathlib import Path
import json, re, sys, zipfile

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
assert root.is_dir(), f"directory not found: {root}"
files = sorted(path for path in root.rglob("*") if path.is_file())
temporary = [
    path for path in root.rglob("*")
    if path.name in {".env", ".DS_Store"}
    or path.suffix.lower() in {".log", ".pyc"}
    or "__pycache__" in path.parts
]
assert not temporary, f"temporary file found: {temporary[0]}"

text = "\n".join(
    re.sub(r"<script\b.*?</script>", "", path.read_text(encoding="utf-8", errors="ignore"), flags=re.S | re.I)
    for path in files
    if path.suffix.lower() not in {".zip", ".png", ".jpg", ".jpeg", ".webp"}
    and "scripts" not in path.parts
)
assert not re.search(
    r"eo_token|eo_time|BEGIN (?:RSA|OPENSSH) PRIVATE KEY|github_pat_[A-Za-z0-9_]+",
    text,
    re.I,
), "credential-like text found"

archives = {}
for name in ("Shu.zip", "svg-art-folio.zip"):
    archive_path = root / name
    assert archive_path.is_file(), f"required archive missing: {name}"
    with zipfile.ZipFile(archive_path) as archive:
        assert archive.testzip() is None, f"corrupt archive: {name}"
        archives[name] = len(archive.namelist())

print(json.dumps({"files": len(files), "credential_scan": True, "archives": archives}, ensure_ascii=False))
