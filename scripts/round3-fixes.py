#!/usr/bin/env python3
"""Round-3 fixes: Support column in every footer, licensing bridge, full audit."""
import glob, json, os, re, zipfile

B = "/Users/jordanthirkle/.openclaw-autoclaw/workspace/byjtt-templates/site"

# 1. strip any stray hidden marker
for f in glob.glob(f"{B}/*.html") + glob.glob(f"{B}/templates/*.html"):
    h = open(f).read()
    if '<p class="footer-h" style="display:none"></p>' in h:
        h = h.replace('<p class="footer-h" style="display:none"></p>', "")
        open(f, "w").write(h)

# 2. Support column before For-agents column in every footer
pages = sorted(glob.glob(f"{B}/*.html") + glob.glob(f"{B}/templates/*.html"))
for f in pages:
    pre = "../" if "/templates/" in f else ""
    h = open(f).read()
    if 'footer-h">Support<' in h:
        continue
    support = (
        "          <div>\n"
        '            <p class="footer-h">Support</p>\n'
        "            <ul>\n"
        '              <li><a href="https://github.com/jordan-thirkle/byjtt-web-design-templates/issues">Issues &amp; contact</a></li>\n'
        f'              <li><a href="{pre}licensing.html">License terms</a></li>\n'
        "            </ul>\n"
        "          </div>\n"
    )
    anchor = "          <div>\n            <p class=\"footer-h\">For agents</p>"
    assert anchor in h, f"anchor missing in {f}"
    h = h.replace(anchor, support + anchor, 1)
    open(f, "w").write(h)
print("support columns added")

# 3. licensing bridge
p = f"{B}/licensing.html"
h = open(p).read()
if "open an issue" not in h:
    h = h.replace(
        "<li>Commercial use requires the Commercial license (paid templates) — this keeps the ladder honest.</li>",
        '<li>Commercial use requires the Commercial license (paid templates). Paid tiers are launching — for commercial use of a free template before that, <a href="https://github.com/jordan-thirkle/byjtt-web-design-templates/issues">open an issue</a> and we will license it directly.</li>',
        1,
    )
    open(p, "w").write(h)
print("licensing bridge added")

# 4. audit
ok = True
for f in glob.glob(f"{B}/**/*.html", recursive=True):
    if "/previews/" in f:
        continue
    base = os.path.dirname(f)
    h = open(f).read()
    for m in re.findall(r'(?:src|href)="([^"#]+)"', h):
        if m.startswith(("http", "mailto:", "tel:", "data:")):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(base, m.split("?")[0]))):
            print("BROKEN:", f, m)
            ok = False
    if 'footer-h">Support<' not in h:
        print("no support col:", f)
        ok = False
    if h.count("aria-current") != 1:
        print("aria-current != 1:", f)
        ok = False
for slug in ("embercraft", "signal"):
    z = glob.glob(f"{B}/assets/templates/{slug}/downloads/*.zip")[0]
    names = zipfile.ZipFile(z).namelist()
    assert any("manifest.json" in n for n in names) and any("LICENSE.txt" in n for n in names) and any("README.md" in n for n in names), slug
cat = json.load(open(f"{B}/catalog.json"))
assert all(e.get("promptKit") for e in cat["entries"]) and cat["count"] == 2
print("zips contain manifest + LICENSE + README; catalog promptKit + count OK")
print("AUDIT:", "PASS" if ok else "FAIL")
