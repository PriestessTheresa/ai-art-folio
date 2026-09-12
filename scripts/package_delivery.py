"""Create a clean, reproducible, single-entry artwork ZIP."""
from pathlib import Path
import hashlib, json, sys, zipfile

source = Path(sys.argv[1] if len(sys.argv) > 1 else "examples/shu/index.html")
out = Path(sys.argv[2] if len(sys.argv) > 2 else "Shu.zip")
assert source.is_file(), f"source file not found: {source}"
out.parent.mkdir(parents=True, exist_ok=True)
info = zipfile.ZipInfo("index.html", date_time=(2020, 1, 1, 0, 0, 0))
info.compress_type = zipfile.ZIP_DEFLATED
info.create_system = 0
info.external_attr = 0o644 << 16
with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    archive.writestr(info, source.read_bytes())
with zipfile.ZipFile(out) as archive:
    assert archive.namelist() == ["index.html"]
    assert archive.testzip() is None
print(json.dumps({"output": str(out), "entries": ["index.html"], "bytes": out.stat().st_size, "sha256": hashlib.sha256(out.read_bytes()).hexdigest()}, ensure_ascii=False))
