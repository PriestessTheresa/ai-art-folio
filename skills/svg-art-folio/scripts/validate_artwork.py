"""Validate an extracted self-contained SVG folio."""
from pathlib import Path
import hashlib, json, re, sys
from xml.etree import ElementTree as ET

path = Path(sys.argv[1] if len(sys.argv) > 1 else "index.html")
s = path.read_text(encoding="utf-8")
markup = re.sub(r"<script\b.*?</script>", "", s, flags=re.S | re.I)
assert not re.search(r"<(?:canvas|image|img|iframe)\b|base64|data:image", markup, re.I), "external or raster resource found"
assert not re.search(r"(?:src|href)=[\"']https?://", markup, re.I), "external resource link found"
svg_match = re.search(r"<svg\b.*?</svg>", s, re.S)
assert svg_match, "SVG root missing"
svg_text = svg_match.group(0)
svg = ET.fromstring(svg_text)
ids = re.findall(r'\bid=["\']([^"\']+)["\']', s)
assert len(ids) == len(set(ids)), "duplicate SVG ids"
data_match = re.search(r'<script id="drawing-data"[^>]*>(.*?)</script>', s, re.S)
assert data_match, "drawing timeline data missing"
data = json.loads(data_match.group(1))
assert data.get("actions"), "drawing timeline missing"
print(json.dumps({"file": str(path), "bytes": path.stat().st_size, "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "svg_ids": len(ids), "actions": len(data["actions"]), "self_contained": True}, ensure_ascii=False))
