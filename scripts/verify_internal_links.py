#!/usr/bin/env python3
"""Verify the acre&key internal-link plan against files in this repo."""

from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
import tempfile
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse
from xml.etree import ElementTree as ET

ROOT = Path("/workspace")
PLAN = Path("/home/ubuntu/.cursor/projects/workspace/uploads/link_plan_aK_2db7.csv")

SKIP_PARTS = {
    "style-guide",
    "landing",
    "scratch",
    "node_modules",
}
VOID = {
    "area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
    "param", "source", "track", "wbr",
}
BANNED = [
    r"\bindependent\b",
    r"\bobjective\b",
    r"\bunbiased\b",
    r"\bluxury\b",
    r"\bpremium\b",
    r"\bbest\b",
    r"\bguaranteed\b",
    r"\bdream home\b",
    r"\bNo\. ?1\b(?!\d)",
    r"\b100\s*%",
]


def load_plan():
    with PLAN.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def html_files():
    files = []
    for path in ROOT.rglob("*.html"):
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        files.append(path)
    return files


def visible_text(page: str) -> str:
    page = re.sub(r"(?is)<script\b[^>]*>.*?</script>", " ", page)
    page = re.sub(r"(?is)<style\b[^>]*>.*?</style>", " ", page)
    page = re.sub(r"(?is)<!--.*?-->", " ", page)
    page = re.sub(r"<[^>]+>", " ", page)
    return html_unescape(page)


def html_unescape(text: str) -> str:
    import html
    return html.unescape(text)


def norm_path(url: str) -> tuple[str, str]:
    parsed = urlparse(url.strip())
    path = parsed.path or "/"
    if not path.endswith("/") and "." not in path.split("/")[-1]:
        path += "/"
    return parsed.netloc.lower(), path


def href_matches(href: str, target: str) -> bool:
    host_h, path_h = norm_path(href)
    host_t, path_t = norm_path(target)
    if path_h != path_t:
        return False
    if host_t == "answers.acrenkey.com":
        return host_h == "answers.acrenkey.com"
    if path_t.startswith("/blogs"):
        return host_h in ("acrenkey.com", "www.acrenkey.com")
    return host_h in ("", "acrenkey.com", "www.acrenkey.com")


def anchor_text(raw: str) -> str:
    text = re.sub(r"<[^>]+>", "", raw)
    return " ".join(html_unescape(text).split())


def file_for_source(url: str) -> Path | None:
    host, path = norm_path(url)
    if host not in ("", "acrenkey.com", "www.acrenkey.com"):
        return None
    if path == "/":
        return ROOT / "index.html"
    rel = path.strip("/")
    candidate = ROOT / rel / "index.html"
    if candidate.exists():
        return candidate
    return None


def extract_anchors(page: str):
    anchors = []
    for match in re.finditer(r"<a\b([^>]*?)>(.*?)</a>", page, flags=re.I | re.S):
        attrs, inner = match.group(1), match.group(2)
        href_match = re.search(r'href\s*=\s*(["\']?)([^"\'\s>]+)\1', attrs, flags=re.I)
        if not href_match:
            continue
        anchors.append((href_match.group(2), anchor_text(inner), match.start()))
    return anchors


def main_slice(page: str) -> str:
    """In-text content: everything outside header, footer and nav.

    Breadcrumbs live in nav, so they do not count. Article copy that sits
    after an early </main> still counts, because readers see it as body copy.
    """
    page = re.sub(r"(?is)<header\b[^>]*>.*?</header>", " ", page)
    page = re.sub(r"(?is)<footer\b[^>]*>.*?</footer>", " ", page)
    page = re.sub(r"(?is)<nav\b[^>]*>.*?</nav>", " ", page)
    return page


class Balancer(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []
        self.errors = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag in ("script", "style"):
            self.skip += 1
        if self.skip:
            return
        if tag in VOID:
            return
        self.stack.append(tag)

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in ("script", "style"):
            if self.skip:
                self.skip -= 1
            return
        if self.skip or tag in VOID:
            return
        if not self.stack:
            self.errors.append(f"extra </{tag}>")
            return
        if self.stack[-1] == tag:
            self.stack.pop()
            return
        if tag in self.stack:
            while self.stack and self.stack[-1] != tag:
                self.errors.append(f"unclosed <{self.stack[-1]}> before </{tag}>")
                self.stack.pop()
            if self.stack:
                self.stack.pop()
        else:
            self.errors.append(f"unexpected </{tag}>")

    def close(self):
        super().close()
        for tag in self.stack:
            self.errors.append(f"unclosed <{tag}>")


def check_balance(page: str) -> list[str]:
    parser = Balancer()
    try:
        parser.feed(page)
        parser.close()
    except Exception as exc:  # noqa: BLE001
        return [str(exc)]
    return parser.errors


def check_jsonld(page: str) -> list[str]:
    errors = []
    for match in re.finditer(
        r'<script\b[^>]*type=(?:["\']application/ld\+json["\']|application/ld\+json)[^>]*>(.*?)</script>',
        page,
        flags=re.I | re.S,
    ):
        raw = match.group(1).strip()
        if not raw:
            continue
        try:
            json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append(str(exc))
    return errors


def check_inline_js(page: str, path: Path) -> list[str]:
    errors = []
    scripts = re.findall(
        r"<script\b(?![^>]*\bsrc=)(?![^>]*application/ld\+json)[^>]*>(.*?)</script>",
        page,
        flags=re.I | re.S,
    )
    for index, script in enumerate(scripts):
        code = script.strip()
        if not code or code.startswith("<!--"):
            continue
        # HTML comments inside scripts
        code = re.sub(r"(?s)<!--.*?-->", "", code).strip()
        if not code:
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as handle:
            handle.write(code)
            name = handle.name
        result = subprocess.run(["node", "--check", name], capture_output=True, text=True)
        Path(name).unlink(missing_ok=True)
        if result.returncode != 0:
            errors.append(result.stderr.strip().splitlines()[-1][:240])
    return errors


def page_base(path: Path) -> str:
    rel = str(path.relative_to(ROOT))
    if rel == "index.html":
        return "https://acrenkey.com/"
    if rel.endswith("/index.html"):
        return "https://acrenkey.com/" + rel[: -len("index.html")]
    return "https://acrenkey.com/" + rel


def local_target(href: str, base: str) -> str | None:
    if href.startswith(("mailto:", "tel:", "javascript:", "#")):
        return None
    absolute = urljoin(base, href)
    parsed = urlparse(absolute)
    host = parsed.netloc.lower()
    if host not in ("", "acrenkey.com", "www.acrenkey.com"):
        return None
    path = parsed.path or "/"
    if not path.endswith("/") and "." not in path.split("/")[-1]:
        path += "/"
    if path.startswith("/blogs"):
        return None
    return path


def repo_file(path: str) -> bool:
    if path in ("/", ""):
        return (ROOT / "index.html").exists()
    rel = path.strip("/")
    if (ROOT / rel / "index.html").exists():
        return True
    if (ROOT / rel).is_file():
        return True
    # redirect stubs
    if rel in ("properties", "home-loan-emi-calculator"):
        return True
    return False


def is_content(path: Path) -> bool:
    rel = str(path.relative_to(ROOT))
    if rel in {
        "404.html",
        "thankyou.html",
        "prestige-evergreen.html",
        "property-template.html",
        "scratch_overview.html",
        "scratch_glance.html",
    }:
        return False
    if rel.startswith(("thankyou/", "properties/", "home-loan-emi-calculator/", "blog/")):
        return False
    text = path.read_text(encoding="utf-8", errors="replace")
    if re.search(r'name=["\']robots["\'][^>]*noindex', text, flags=re.I):
        return False
    if re.search(r'content=["\'][^"\']*noindex', text, flags=re.I):
        return False
    return True


def main() -> int:
    plan = load_plan()
    files = html_files()
    pages = {path: path.read_text(encoding="utf-8", errors="replace") for path in files}
    anchors = {path: extract_anchors(page) for path, page in pages.items()}

    missing_links = []
    present = 0
    for row in plan:
        if "partners" in row["target"]:
            missing_links.append({**row, "reason": "partners page removed on this branch"})
            continue
        path = file_for_source(row["source"])
        if path is None or path not in anchors:
            missing_links.append({**row, "reason": "source page is not in this repo"})
            continue
        found = False
        for href, text, _pos in anchors[path]:
            if href_matches(href, row["target"]) and text == " ".join(row["anchor"].split()):
                found = True
                break
        if found:
            present += 1
        else:
            missing_links.append({**row, "reason": "anchor not found on source page"})

    blog_hits = []
    broken = []
    banned_hits = []
    balance_bad = []
    json_bad = []
    js_bad = []
    for path, page in pages.items():
        rel = str(path.relative_to(ROOT))
        base = page_base(path)
        for href, _text, _pos in anchors[path]:
            if re.search(r"/blog/?($|[?#])", href) or "/blog/" in href:
                blog_hits.append((rel, href))
            local = local_target(href, base)
            if local and not repo_file(local):
                broken.append((rel, href, local))
        text = visible_text(page)
        for pattern in BANNED:
            if re.search(pattern, text, flags=re.I):
                banned_hits.append((rel, pattern))
                break
        if "Acre&" in page or "Acre &" in page or "AcreNKey" in page or "Acre and Key" in page:
            visible = re.sub(r"(?is)<script\b[^>]*>.*?</script>", " ", page)
            visible = re.sub(r"(?is)<style\b[^>]*>.*?</style>", " ", visible)
            visible = re.sub(r"(?is)<!--.*?-->", " ", visible)
            visible = re.sub(r"Acrenkey\s+Realty", " ", visible)
            if re.search(r"Acre\s*(?:&amp;|&)\s*Key|AcreNKey|Acre and Key", visible):
                banned_hits.append((rel, "brand-spelling"))
        errors = check_balance(page)
        if errors:
            balance_bad.append((rel, errors[:4]))
        jerrors = check_jsonld(page)
        if jerrors:
            json_bad.append((rel, jerrors[:2]))

    # Inline JS on a sample plus every changed content page is expensive.
    # Check content pages only.
    content_paths = [path for path in pages if is_content(path)]
    for path in content_paths:
        errors = check_inline_js(pages[path], path)
        if errors:
            js_bad.append((str(path.relative_to(ROOT)), errors[:2]))

    # Inlinks
    path_by_url = {}
    for path in content_paths:
        rel = str(path.relative_to(ROOT))
        if rel == "index.html":
            url = "/"
        else:
            url = "/" + rel[: -len("index.html")]
        path_by_url[url] = path

    referrers = defaultdict(set)
    any_referrers = defaultdict(set)
    for path, page in pages.items():
        base = page_base(path)
        body = main_slice(page)
        for href, _text, _pos in extract_anchors(body):
            local = local_target(href, base)
            if local in path_by_url and path_by_url[local] != path:
                referrers[local].add(str(path.relative_to(ROOT)))
        for href, _text, _pos in anchors[path]:
            local = local_target(href, base)
            if local in path_by_url and path != path_by_url[local]:
                any_referrers[local].add(str(path.relative_to(ROOT)))

    weak = []
    orphans = []
    for url, path in path_by_url.items():
        rel = str(path.relative_to(ROOT))
        # Legal pages are linked in the footer; they are not editorial content.
        if rel.startswith(("privacy-policy/", "terms-of-service/", "rera-disclaimer/")):
            if len(any_referrers[url]) == 0:
                orphans.append(rel)
            continue
        if len(any_referrers[url]) == 0:
            orphans.append(rel)
        if len(referrers[url]) < 5:
            weak.append((rel, len(referrers[url]), sorted(referrers[url])[:8]))

    sitemap_errors = []
    try:
        ET.parse(ROOT / "sitemap.xml")
    except ET.ParseError as exc:
        sitemap_errors.append(str(exc))

    # Hub URLs present in sitemap
    hub_missing = []
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    for path in (ROOT / "property").glob("area/*/index.html"):
        loc = "https://acrenkey.com/property/area/" + path.parent.name + "/"
        if loc not in sitemap:
            hub_missing.append(loc)
    for path in (ROOT / "property").glob("developer/*/index.html"):
        loc = "https://acrenkey.com/property/developer/" + path.parent.name + "/"
        if loc not in sitemap:
            hub_missing.append(loc)

    report = {
        "planned": len(plan),
        "present": present,
        "missing": len(missing_links),
        "missing_sample": [
            {
                "source": row["source"],
                "target": row["target"],
                "anchor": row["anchor"],
                "reason": row["reason"],
            }
            for row in missing_links[:30]
        ],
        "blog_links": blog_hits[:20],
        "blog_count": len(blog_hits),
        "broken_internal": broken[:30],
        "broken_count": len(broken),
        "banned": banned_hits[:40],
        "banned_count": len(banned_hits),
        "balance_bad": balance_bad[:15],
        "balance_count": len(balance_bad),
        "jsonld_bad": json_bad[:10],
        "jsonld_count": len(json_bad),
        "js_bad": js_bad[:10],
        "js_count": len(js_bad),
        "orphans": orphans,
        "weak_count": len(weak),
        "weak_sample": weak[:40],
        "sitemap_errors": sitemap_errors,
        "hubs_missing_from_sitemap": hub_missing,
        "content_pages": len(path_by_url),
    }
    out = ROOT / "scripts" / "link-verify-report.json"
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({k: report[k] for k in report if k not in ("missing_sample", "weak_sample", "balance_bad", "banned")}, indent=2))
    print("missing sample:")
    for row in report["missing_sample"][:15]:
        print(" -", row["reason"], row["anchor"][:60], "->", row["target"][:80])
    print("weak sample:")
    for row in weak[:20]:
        print(" -", row[0], row[1])
    return 0


if __name__ == "__main__":
    sys.exit(main())
