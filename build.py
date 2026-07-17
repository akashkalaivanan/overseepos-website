"""Build a clean, hostable OverseePOS static site from saved HTML assets."""
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent
STATIC = ROOT / "static"

STATIC.mkdir(exist_ok=True)

shutil.copy2(SOURCE / "main.715f0c28.js.download", STATIC / "main.js")
shutil.copy2(SOURCE / "main.a59ad216.css", STATIC / "main.css")

html = (SOURCE / "saved_resource(1).html").read_text(encoding="utf-8")

# Strip Emergent / analytics scripts and preview logger
html = re.sub(r'<script[^>]*src="\./emergent-main\.js\.download"[^>]*></script>', "", html)
html = re.sub(r'<script[^>]*src="\./array\.js\.download"[^>]*></script>', "", html)
html = re.sub(r'<script[^>]*>window\.addEventListener\("error".*?</script>', "", html, flags=re.DOTALL)
html = re.sub(r'<script>!function\([^<]*posthog\.init.*?</script>', "", html, flags=re.DOTALL)

# Fix asset paths
html = html.replace("./main.715f0c28.js.download", "./static/main.js")
html = html.replace("./main.a59ad216.css", "./static/main.css")
html = html.replace('./css2(3)', "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700;800&display=swap")

# Point internal links to local anchors
html = re.sub(
    r"https://modern-checkout-11\.preview\.(?:static\.)?emergentagent\.com/#?",
    "#",
    html,
)

# Update metadata
html = html.replace(
    'content="A product of emergent.sh"',
    'content="Modern POS system for UAE restaurants, retail and salons. Unified billing, inventory and multi-store management."',
)
html = html.replace('content="#000000"', 'content="#f97316"')

# Ensure doctype and lang are clean
if not html.strip().lower().startswith("<!doctype"):
    html = "<!DOCTYPE html>\n" + html

out = ROOT / "index.html"
out.write_text(html, encoding="utf-8")
print(f"Built {out} ({out.stat().st_size:,} bytes)")
