#!/usr/bin/env python3
"""Place the acre&key internal-link plan on main pages, calculators and /property/."""

from __future__ import annotations

import csv
import html as html_lib
import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse, urlunparse

ROOT = Path("/workspace")
PLAN = Path("/home/ubuntu/.cursor/projects/workspace/uploads/link_plan_aK_2db7.csv")
HUBS = Path("/home/ubuntu/.cursor/projects/workspace/uploads/05_Hub_Structure_9029.csv")
DATA_JS = ROOT / "property" / "properties-data.js"

REL = (
    "font-family:Manrope,sans-serif;font-size:0.95rem;line-height:1.6;"
    "color:#55555A;margin:0.85rem 0 1.1rem;"
)
A_STYLE = "color:#804526;text-decoration:underline;text-underline-offset:3px;"
CHIP = (
    "display:inline-block;margin:0 0.4rem 0.4rem 0;padding:0.35rem 0.7rem;"
    "border:0.5px solid rgba(85,85,90,0.2);border-radius:4px;color:#804526;"
    "text-decoration:none;font-family:Manrope,sans-serif;font-size:0.82rem;font-weight:600;"
)

ZONE_OF = {
    "whitefield": "east-bengaluru",
    "sarjapur-road": "east-bengaluru",
    "budigere-cross": "east-bengaluru",
    "kr-puram": "east-bengaluru",
    "varthur": "east-bengaluru",
    "panathur": "east-bengaluru",
    "east-bengaluru": "east-bengaluru",
    "devanahalli": "north-bengaluru",
    "bagalur": "north-bengaluru",
    "yelahanka": "north-bengaluru",
    "tumkur-road": "north-bengaluru",
    "thanisandra": "north-bengaluru",
    "north-bengaluru": "north-bengaluru",
    "bannerghatta-road": "south-bengaluru",
    "kanakapura-road": "south-bengaluru",
    "hosur-road": "south-bengaluru",
    "south-bengaluru": "south-bengaluru",
    "mysore-road": "west-bengaluru",
    "west-bengaluru": "west-bengaluru",
}
ZONE_LABEL = {
    "east-bengaluru": "East Bengaluru",
    "north-bengaluru": "North Bengaluru",
    "south-bengaluru": "South Bengaluru",
    "west-bengaluru": "West Bengaluru",
}
ZONES = list(ZONE_LABEL)

NAV_ITEMS = [
    ("/property/", "Properties"),
    ("/calculators/", "Calculators"),
    ("https://acrenkey.com/blogs/", "Blog"),
    ("https://answers.acrenkey.com/", "Answers"),
    ("/contact/", "Contact"),
]

FOOTER_LINKS = [
    ("/property/", "Properties"),
    ("/property/area/east-bengaluru/", "East Bengaluru"),
    ("/property/area/north-bengaluru/", "North Bengaluru"),
    ("/property/area/south-bengaluru/", "South Bengaluru"),
    ("/property/area/west-bengaluru/", "West Bengaluru"),
    ("/calculators/", "Calculators"),
    ("https://acrenkey.com/blogs/", "Blog"),
    ("https://answers.acrenkey.com/", "Answers"),
    ("/", "Home"),
    ("/property-consultant-bengaluru/", "Property Consultant in Bengaluru"),
    ("/careers/", "Careers"),
    ("/contact/", "Contact"),
    ("/privacy-policy/", "Privacy Policy"),
    ("/terms-of-service/", "Terms of Service"),
    ("/rera-disclaimer/", "RERA Disclaimer"),
]


def load_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def esc(text: str) -> str:
    return html_lib.escape(text, quote=True)


def href_for(url: str) -> str:
    parsed = urlparse(url.strip())
    path = parsed.path or "/"
    if not path.endswith("/") and "." not in path.split("/")[-1]:
        path += "/"
    if "partners" in path:
        return ""
    if parsed.netloc == "answers.acrenkey.com":
        return urlunparse(parsed._replace(scheme="https", path=path))
    if path == "/blogs/" or path.startswith("/blogs/"):
        return "https://acrenkey.com" + path
    if parsed.netloc in ("", "acrenkey.com", "www.acrenkey.com"):
        return path
    return urlunparse(parsed._replace(path=path))


def a_tag(url: str, anchor: str) -> str:
    href = href_for(url)
    return f'<a href="{esc(href)}" style="{A_STYLE}">{esc(anchor)}</a>'


def related(links: list[tuple[str, str]], lead: str = "Related") -> str:
    body = " · ".join(a_tag(url, anchor) for url, anchor in links)
    return (
        f'<p class="ak-inline-related" data-ak-rel="1" style="{REL}">'
        f'<span style="color:#804526;font-weight:600;">{lead}.</span> {body}</p>'
    )


def sentence(text_html: str) -> str:
    return f'<p class="ak-inline-related" data-ak-rel="1" style="{REL}">{text_html}</p>'


def url_path(url: str) -> str:
    parsed = urlparse(url.strip())
    path = parsed.path or "/"
    if not path.endswith("/") and "." not in path.split("/")[-1]:
        path += "/"
    return path


def source_file(url: str) -> Path | None:
    path = url_path(url)
    if path == "/":
        return ROOT / "index.html"
    rel = path.strip("/")
    candidate = ROOT / rel / "index.html"
    if candidate.exists():
        return candidate
    direct = ROOT / rel
    if direct.suffix == ".html" and direct.exists():
        return direct
    return None


def bucket(placement: str) -> str:
    if placement == "Breadcrumb":
        return "breadcrumb"
    if placement.startswith('"About the developer"') or "About the developer" in placement:
        return "developer"
    if placement.startswith("FAQ"):
        return "faq"
    if placement.startswith("Price / payment-plan"):
        return "price_emi"
    if placement.startswith("Price section"):
        return "price_stamp"
    if placement.startswith("Floor plans"):
        return "floor"
    if "Similar properties" in placement:
        return "similar"
    if placement.startswith("Investment outlook"):
        return "investment"
    if placement.startswith("Location"):
        return "location"
    if "How this works" in placement:
        return "how"
    if "Next step" in placement:
        return "next"
    if placement.startswith("Results panel"):
        return "results"
    if "Filter chips" in placement or "Browse by" in placement:
        return "browse"
    if "Area list" in placement:
        return "areas"
    if "Header nav" in placement or "header nav" in placement:
        return "nav"
    if "Learn before you buy" in placement:
        return "learn"
    if "Explore by area" in placement:
        return "explore"
    if "Tools & guides" in placement or "Tools &amp; guides" in placement:
        return "tools"
    if placement.startswith("Hero"):
        return "hero"
    if "Closing paragraph" in placement:
        return "closing"
    if "final CTA" in placement:
        return "cta"
    if "resources section" in placement:
        return "resources"
    if "role list" in placement:
        return "roles"
    if "after the hero" in placement:
        return "after_hero"
    match = re.search(r'section "([^"]+)"', placement)
    if match:
        return "sec:" + match.group(1)
    return "fallback"


def iter_headings(page: str):
    for match in re.finditer(r"<h([1-6])\b[^>]*>(.*?)</h\1>", page, flags=re.I | re.S):
        text = re.sub(r"<[^>]+>", "", match.group(2))
        text = " ".join(html_lib.unescape(text).split())
        yield match.end(), text


def find_heading(page: str, needles: list[str]) -> int | None:
    heads = list(iter_headings(page))
    for needle in needles:
        lowered = needle.lower()
        for end, text in heads:
            if lowered in text.lower():
                return end
    return None


def heading_before_marker(page: str, marker: str) -> int | None:
    heads = list(iter_headings(page))
    for index, (end, text) in enumerate(heads):
        if marker.lower() in text.lower() and index:
            return heads[index - 1][0]
    return None


NEEDLES = {
    "faq": ["Frequently asked questions", "Frequently Asked Questions", "FAQ"],
    "how": ["How do you use", "How this", "How the", "How Karnataka", "Formula"],
    "next": ["Related calculators", "Related Calculators"],
    "results": ["Your result", "Your Result", "Results"],
    "price_emi": ["On-Road Cost", "True Cost", "What Will You Actually Pay", "Cost Sheet", "What Gets Added"],
    "price_stamp": ["On-Road Cost", "True Cost", "What Will You Actually Pay", "What Gets Added", "Pricing & Negotiation", "Pricing"],
    "floor": ["Unit Typology", "Plot Dimension", "Floor Plan", "Space Analysis", "Layout Specifications"],
    "investment": ["Area Appreciation", "Investment", "Appreciation"],
    "location": ["Connectivity", "Corridor", "Growth Corridor", "Kadugodi"],
    "similar": ["You may also want to compare", "Similar properties"],
    "developer": [],
    "cta": ["Talk through the home", "Schedule Your Consultation"],
    "resources": ["What Real Estate Consultancy", "Resources"],
    "roles": ["Explore Opportunities"],
    "closing": ["Book a consultation", "Get in touch"],
}


def placement_pos(page: str, key: str) -> int | None:
    if key == "developer":
        match = re.search(r"</h1>", page, flags=re.I)
        return match.end() if match else None
    if key.startswith("sec:"):
        found = find_heading(page, [key[4:]])
        if found is not None:
            return found
        return None
    needles = NEEDLES.get(key, [])
    if needles:
        found = find_heading(page, needles)
        if found is not None:
            return found
    if key == "investment":
        return heading_before_marker(page, "RERA")
    if key == "location":
        return heading_before_marker(page, "RERA")
    if key in ("tools", "fallback", "browse"):
        return None
    return None


def footer_pos(page: str) -> int:
    match = re.search(r"<footer\b", page, flags=re.I)
    if match:
        return match.start()
    main = page.lower().rfind("</main>")
    if main != -1:
        return main
    return len(page)


def apply_inserts(page: str, inserts: list[tuple[int, str]]) -> str:
    merged: dict[int, list[str]] = defaultdict(list)
    for pos, snippet in inserts:
        merged[pos].append(snippet)
    for pos in sorted(merged, reverse=True):
        block = "".join(merged[pos])
        page = page[:pos] + block + page[pos:]
    return page


def load_properties() -> dict[str, dict]:
    text = DATA_JS.read_text(encoding="utf-8")
    data = json.loads(text[text.find("[") : text.rfind("]") + 1])
    return {row["slug"]: row for row in data}


def crumb_html(parts: list[tuple[str, str | None]]) -> str:
    bits = []
    for index, (label, href) in enumerate(parts):
        if index:
            bits.append('<li><span class="separator">›</span></li>')
        if href:
            bits.append(f'<li><a href="{esc(href)}">{esc(label)}</a></li>')
        else:
            bits.append(f'<li class="current" aria-current="page">{esc(label)}</li>')
    return '<ol class="page-breadcrumb" style="margin:0;">' + "".join(bits) + "</ol>"


def crumb_json(parts: list[tuple[str, str]]) -> list[dict]:
    items = []
    for index, (label, href) in enumerate(parts, start=1):
        items.append(
            {
                "@type": "ListItem",
                "position": index,
                "name": label,
                "item": href,
            }
        )
    return items


def replace_breadcrumb_html(page: str, ol: str) -> str:
    updated, count = re.subn(
        r'<ol\b[^>]*class=["\']?page-breadcrumb["\']?[^>]*>.*?</ol>',
        ol,
        page,
        count=1,
        flags=re.S | re.I,
    )
    return updated if count else page


def replace_breadcrumb_json(page: str, items: list[dict]) -> str:
    pattern = re.compile(
        r'(<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>)(.*?)(</script>)',
        flags=re.S | re.I,
    )

    def repl(match: re.Match) -> str:
        raw = match.group(2).strip()
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            return match.group(0)
        changed = False

        def walk(node):
            nonlocal changed
            if isinstance(node, dict):
                kind = node.get("@type")
                kinds = kind if isinstance(kind, list) else [kind]
                if "BreadcrumbList" in kinds and "itemListElement" in node:
                    node["itemListElement"] = items
                    changed = True
                for value in node.values():
                    walk(value)
            elif isinstance(node, list):
                for value in node:
                    walk(value)

        walk(data)
        if not changed:
            return match.group(0)
        dumped = json.dumps(data, ensure_ascii=False, indent=2)
        return match.group(1) + "\n" + dumped + "\n" + match.group(3)

    return pattern.sub(repl, page)


def current_crumb_label(page: str, fallback: str) -> str:
    match = re.search(
        r'<li[^>]*class=["\'][^"\']*current[^"\']*["\'][^>]*>(.*?)</li>',
        page,
        flags=re.S | re.I,
    )
    if not match:
        return fallback
    text = re.sub(r"<[^>]+>", "", match.group(1))
    text = " ".join(html_lib.unescape(text).split())
    return text or fallback


def update_project_breadcrumb(page: str, slug: str, props: dict, area_anchor: dict) -> str:
    if slug not in area_anchor:
        return page
    area_slug, anchor = area_anchor[slug]
    zone = ZONE_OF.get(area_slug, area_slug)
    name = current_crumb_label(page, props.get(slug, {}).get("name", slug))
    parts_html: list[tuple[str, str | None]] = [
        ("Home", "/"),
        ("Properties", "/property/"),
    ]
    parts_abs: list[tuple[str, str]] = [
        ("Home", "https://acrenkey.com/"),
        ("Properties", "https://acrenkey.com/property/"),
    ]
    if area_slug in ZONE_LABEL and area_slug == zone and area_slug in ZONE_LABEL:
        # Project sits on the zone hub itself.
        parts_html.append((anchor, f"/property/area/{zone}/"))
        parts_abs.append((anchor, f"https://acrenkey.com/property/area/{zone}/"))
    else:
        parts_html.append((ZONE_LABEL[zone], f"/property/area/{zone}/"))
        parts_abs.append((ZONE_LABEL[zone], f"https://acrenkey.com/property/area/{zone}/"))
        parts_html.append((anchor, f"/property/area/{area_slug}/"))
        parts_abs.append((anchor, f"https://acrenkey.com/property/area/{area_slug}/"))
    parts_html.append((name, None))
    parts_abs.append((name, f"https://acrenkey.com/property/{slug}/"))
    page = replace_breadcrumb_html(page, crumb_html(parts_html))
    page = replace_breadcrumb_json(page, crumb_json(parts_abs))
    return page


def replace_desktop_nav(page: str) -> str:
    def repl(match: re.Match) -> str:
        items = "".join(f'<li><a href="{href}">{esc(label)}</a></li>' for href, label in NAV_ITEMS)
        open_tag = match.group(0).split(">", 1)[0] + ">"
        return open_tag + items + "</ul>"

    return re.sub(
        r"<ul\b[^>]*class=[\"']?nav-links[\"']?[^>]*>.*?</ul>",
        repl,
        page,
        count=1,
        flags=re.S | re.I,
    )


def replace_mobile_nav(page: str) -> str:
    def repl(match: re.Match) -> str:
        block = match.group(0)
        labels = list(
            re.finditer(
                r"(<span\b[^>]*class=[\"']?mobile-nav-label[\"']?[^>]*>)(.*?)(</span>)",
                block,
                flags=re.S | re.I,
            )
        )
        hrefs = list(re.finditer(r"\bhref\s*=\s*([\"']?)([^\"'\s>]+)\1", block, flags=re.I))
        if len(labels) < 5 or len(hrefs) < 5:
            links = "".join(
                f'<a href="{href}" class=mobile-nav-item><span class=mobile-nav-label>{esc(label)}</span></a>'
                for href, label in NAV_ITEMS
            )
            return "<nav class=mobile-nav-list>" + links + "</nav>"
        chars = list(block)
        # Replace from the end so offsets stay valid.
        for index in range(4, -1, -1):
            href, label = NAV_ITEMS[index]
            href_match = hrefs[index]
            label_match = labels[index]
            chars[label_match.start(2) : label_match.end(2)] = list(label)
            chars[href_match.start(2) : href_match.end(2)] = list(href)
        return "".join(chars)

    return re.sub(
        r"<nav\b[^>]*class=[\"']?mobile-nav-list[\"']?[^>]*>.*?</nav>",
        repl,
        page,
        count=1,
        flags=re.S | re.I,
    )


def replace_footer_nav(page: str) -> str:
    links = "\n".join(f'        <a href="{href}">{esc(label)}</a>' for href, label in FOOTER_LINKS)

    def repl(match: re.Match) -> str:
        open_tag = match.group(0).split(">", 1)[0] + ">"
        return open_tag + "\n" + links + "\n      </nav>"

    return re.sub(
        r"<nav\b[^>]*class=[\"'][^\"']*ak-footer-links[^\"']*[\"'][^>]*>.*?</nav>",
        repl,
        page,
        count=1,
        flags=re.S | re.I,
    )


def fix_href_hygiene(page: str) -> str:
    def repl(match: re.Match) -> str:
        prefix, quote, url, endq = match.group(1), match.group(2), match.group(3), match.group(4)
        parsed = urlparse(url)
        path = parsed.path or ""
        host = parsed.netloc
        if host in ("", "acrenkey.com", "www.acrenkey.com"):
            bare = path.rstrip("/")
            if bare in ("/blog", "/blogs"):
                return f"{prefix}{quote}https://acrenkey.com/blogs/{endq}"
            if path.startswith("/blog/"):
                rest = path[len("/blog/") :]
                if rest and not rest.endswith("/"):
                    rest += "/"
                return f"{prefix}{quote}https://acrenkey.com/blogs/{rest}{endq}"
            if bare in ("/privacy-policy", "/terms-of-service", "/property-consultant-bengaluru", "/contact", "/careers", "/calculators", "/property", "/rera-disclaimer"):
                new_path = bare + "/"
                if host:
                    return f"{prefix}{quote}https://acrenkey.com{new_path}{endq}"
                return f"{prefix}{quote}{new_path}{endq}"
        return match.group(0)

    return re.sub(r"(href\s*=\s*)([\"'])(.*?)(\2)", repl, page, flags=re.I | re.S)


def cap_case(word: str, sample: str) -> str:
    if sample.isupper():
        return word.upper()
    if sample[:1].isupper():
        return word[:1].upper() + word[1:]
    return word


def clean_text(text: str) -> str:
    if not text:
        return text

    def sub(pattern, repl, flags=re.I):
        nonlocal text
        text = re.sub(pattern, repl, text, flags=flags)

    sub(r"\b100\s*%\s*Capital Return", "Capital returned")
    sub(r"\b100\s*%\s*secure", "fully secure")
    sub(r"\b100\s*%\s*DG", "Full DG", flags=0)
    sub(r"\b100\s*%", "full")
    sub(r"\bdream homes?\b", "home")
    sub(r"\bultra-luxury\b", lambda m: cap_case("large-format", m.group(0)))
    sub(r"\bluxury\b", lambda m: cap_case("institutional-grade", m.group(0)))
    sub(r"(₹\s?[\d.,]+\s?L)\s+Premium\b", r"\1 mark-up")
    sub(r"\bpremium entry price\b", "higher entry price")
    sub(r"\bpremium customer\b", "careful customer")
    sub(r"\bpremium positioning\b", "higher-spec positioning")
    sub(r"\bpremium\b", "A-grade")
    sub(r"\bunbiased\b", lambda m: cap_case("structured", m.group(0)))
    sub(
        r"\bindependent\s+(legal|professional|technical|tax|structural)\b",
        lambda m: cap_case("separate", m.group(0)) + " " + m.group(1),
    )
    sub(r"\bindependent buyer\b", lambda m: cap_case("buyer-first", m.group(0)))
    sub(r"\bindependent\b", lambda m: cap_case("buyer-first", m.group(0)))
    sub(r"\bobjectives\b", lambda m: cap_case("goals", m.group(0)))
    sub(r"\bobjective\b", lambda m: cap_case("aim", m.group(0)))
    sub(r"\bBest-Fit\b", "Strong-Fit", flags=0)
    sub(r"\bbest-fit\b", "strong-fit")
    sub(r"\bthe best\b", "a sound")
    sub(r"\bbest suited\b", "well suited")
    sub(r"\bwhat['’]s best\b", "what serves")
    sub(r"\bbest fits\b", "fits")
    sub(r"\bBest\b", "Strong", flags=0)
    sub(r"\bbest\b", "strong")
    sub(r"\bguaranteed\b", "promised")
    sub(r"\bNo\. ?1\b(?!\d)", "noted", flags=0)
    text = re.sub(r"Acre\s*&amp;\s*Key", "acre&amp;key", text)
    text = re.sub(r"Acre\s*&\s*Key", "acre&amp;key", text)
    text = re.sub(r"Acre\s+and\s+Key", "acre&amp;key", text, flags=re.I)
    text = re.sub(
        r"(?<![\w./@])Acrenkey(?!\.com)(?!\s+Realty)\b",
        "acre&amp;key",
        text,
        flags=re.I,
    )
    return text


def compliance_phrases(page: str) -> str:
    replacements = [
        (
            "receiving commissions or referral fees from developers",
            "acting as a sales partner on some projects",
        ),
        (
            "receive commissions or referral fees from developers",
            "act as a sales partner on some projects",
        ),
        (
            "receive a commission or referral fee from a developer",
            "act as a sales partner on a project",
        ),
        ("commissions from developers", "a sales-partner role on some projects"),
        ("paid by developers", "a sales partner on a project"),
        (
            "Does Acre&Key receive a sales-partner role on some projects?",
            "Does Acre&Key act as a sales partner on some projects?",
        ),
        (
            "Does acre&amp;key receive a sales-partner role on some projects?",
            "Does acre&amp;key act as a sales partner on some projects?",
        ),
    ]
    for old, new in replacements:
        page = page.replace(old, new)
    # The question rewrite above can miss the original if the commission phrase
    # was replaced inside a longer question. Cover the original question too.
    page = page.replace(
        "Does Acre&Key receive commissions from developers?",
        "Does Acre&Key act as a sales partner on some projects?",
    )
    page = page.replace(
        "receive commissions from developers?",
        "act as a sales partner on some projects?",
    )
    return page


ATTRS = ("alt", "title", "content", "aria-label", "placeholder")


def rewrite_visible(page: str) -> str:
    masked = re.compile(
        r"(?is)(<script\b[^>]*>.*?</script>|<style\b[^>]*>.*?</style>|<!--.*?-->)"
    )
    parts = []
    pos = 0
    for match in masked.finditer(page):
        parts.append(rewrite_segment(page[pos : match.start()]))
        parts.append(match.group(0))
        pos = match.end()
    parts.append(rewrite_segment(page[pos:]))
    return "".join(parts)


def rewrite_segment(segment: str) -> str:
    bits = re.split(r"(<[^>]+>)", segment)
    for index, bit in enumerate(bits):
        if bit.startswith("<"):
            bits[index] = rewrite_tag(bit)
        else:
            bits[index] = clean_text(bit)
    return "".join(bits)


def rewrite_tag(tag: str) -> str:
    def repl(match: re.Match) -> str:
        name, quote, value = match.group(1), match.group(2), match.group(3)
        if name.lower() not in ATTRS:
            return match.group(0)
        if name.lower() == "content" and value.strip().startswith(("http://", "https://", "/", "#")):
            return match.group(0)
        return f"{name}={quote}{clean_text(value)}{quote}"

    return re.sub(r"([:\w-]+)\s*=\s*([\"'])(.*?)\2", repl, tag, flags=re.S)


def guide_label(path: str) -> str:
    slug = path.strip("/").split("/")[-1]
    slug = re.sub(r"-property-rates.*", "", slug)
    slug = re.sub(r"-for-homebuyers$", "", slug)
    words = slug.replace("-", " ")
    small = {"in", "on", "vs", "and", "for", "the", "of"}
    titled = []
    for index, word in enumerate(words.split()):
        if index and word in small:
            titled.append(word)
        else:
            titled.append(word[:1].upper() + word[1:])
    return " ".join(titled)


def fit_len(text: str, low: int, high: int, filler: str) -> str:
    text = " ".join(text.split())
    guard = 0
    while len(text) < low and guard < 4:
        text = (text + " " + filler).strip()
        guard += 1
    if len(text) > high:
        cut = text[: high - 1].rsplit(" ", 1)[0]
        text = cut if len(cut) >= low else text[:high].rstrip()
    return text


def project_card(row: dict) -> str:
    name = row["name"]
    url = row["url"] if row["url"].endswith("/") else row["url"] + "/"
    place = row.get("sublocation") or row.get("location") or "Bengaluru"
    config = row.get("config") or ""
    size = row.get("sizeRange") or ""
    possession = row.get("possession") or ""
    rera = row.get("rera") or []
    if isinstance(rera, str):
        rera = [rera]
    rera_text = ", ".join(rera)
    thumb = row.get("heroImg") or ""
    image = ""
    if thumb:
        image_path = ROOT / "property" / thumb
        if image_path.exists():
            image = (
                f'<img src="../../{esc(thumb)}" alt="{esc(name)} in {esc(place)}" '
                f'width="640" height="309" loading="lazy" decoding="async" '
                f'style="width:100%;height:168px;object-fit:cover;border-radius:4px;display:block;margin-bottom:0.75rem;">'
            )
    facts = [row.get("developer") or "", place]
    fact_line = " · ".join(bit for bit in facts if bit)
    spec = " · ".join(bit for bit in (config, size) if bit)
    bits = [
        f'<article class="hub-card" style="border:0.5px solid rgba(85,85,90,0.2);border-radius:4px;padding:1rem;background:#FAFAFA;">',
        image,
        f'<h2 style="font-family:\'Cormorant Garamond\',serif;font-weight:400;font-size:1.55rem;line-height:1.2;margin:0 0 0.4rem;"><a href="{esc(url)}" style="color:#2B2D31;text-decoration:none;">{esc(name)}</a></h2>',
        f'<p style="margin:0;color:#55555A;font-family:Manrope,sans-serif;font-size:0.92rem;line-height:1.55;">{esc(fact_line)}</p>',
    ]
    if spec:
        bits.append(
            f'<p style="margin:0.35rem 0 0;color:#55555A;font-family:Manrope,sans-serif;font-size:0.92rem;line-height:1.55;">{esc(spec)}</p>'
        )
    if possession:
        bits.append(
            f'<p style="margin:0.35rem 0 0;color:#55555A;font-family:Manrope,sans-serif;font-size:0.92rem;line-height:1.55;">{esc(possession)}</p>'
        )
    if rera_text:
        bits.append(
            f'<p style="margin:0.35rem 0 0;color:#55555A;font-family:Manrope,sans-serif;font-size:0.88rem;line-height:1.55;">Karnataka RERA: {esc(rera_text)}</p>'
        )
    bits.append("</article>")
    return "".join(bits)


def json_ld_hub(canonical: str, name: str, description: str, crumbs: list[tuple[str, str]], projects: list[dict]) -> str:
    graph = [
        {
            "@type": "CollectionPage",
            "@id": canonical + "#webpage",
            "url": canonical,
            "name": name,
            "description": description,
            "inLanguage": "en-IN",
            "isPartOf": {"@id": "https://acrenkey.com/#website"},
            "breadcrumb": {"@id": canonical + "#breadcrumb"},
            "dateModified": "2026-10-23",
            "publisher": {"@id": "https://acrenkey.com/#organization"},
        },
        {
            "@type": "BreadcrumbList",
            "@id": canonical + "#breadcrumb",
            "itemListElement": crumb_json(crumbs),
        },
        {
            "@type": "ItemList",
            "@id": canonical + "#list",
            "name": name,
            "itemListOrder": "https://schema.org/ItemListOrderAscending",
            "numberOfItems": len(projects),
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": index,
                    "name": row["name"],
                    "url": "https://acrenkey.com" + (row["url"] if row["url"].endswith("/") else row["url"] + "/"),
                }
                for index, row in enumerate(projects, start=1)
            ],
        },
        {
            "@type": "WebSite",
            "@id": "https://acrenkey.com/#website",
            "name": "acre&key",
            "url": "https://acrenkey.com/",
            "publisher": {"@id": "https://acrenkey.com/#organization"},
        },
        {
            "@type": "Organization",
            "@id": "https://acrenkey.com/#organization",
            "name": "acre&key",
            "legalName": "Acrenkey Realty LLP",
            "url": "https://acrenkey.com/",
        },
    ]
    payload = {"@context": "https://schema.org", "@graph": graph}
    return json.dumps(payload, ensure_ascii=False, indent=2)


def render_hub(
    kind: str,
    slug: str,
    h1: str,
    projects: list[dict],
    crumbs: list[tuple[str, str]],
    intro_html: str,
    extra_html: str,
    description: str,
) -> str:
    canonical = f"https://acrenkey.com/property/{kind}/{slug}/"
    title = fit_len(f"Reviewed projects in {h1.replace('Property in ', '')} | acre&key", 50, 60, "Bengaluru")
    if kind == "developer":
        title = fit_len(f"{h1} | acre&key", 50, 60, "Bengaluru")
    meta = fit_len(description, 140, 160, "Configuration, size, possession and Karnataka RERA numbers come from each project page.")
    crumb_visible = []
    for index, (label, href) in enumerate(crumbs):
        if index == len(crumbs) - 1:
            crumb_visible.append((label, None))
        else:
            path = urlparse(href).path
            crumb_visible.append((label, path))
    header = (ROOT / "property" / "index.html").read_text(encoding="utf-8")
    header_html = re.search(r"<header class=\"header-nav\".*?</header>", header, flags=re.S).group(0)
    footer_html = re.search(r"<footer class=\"site-footer ak-footer\".*?</footer>", header, flags=re.S).group(0)
    ld = json_ld_hub(canonical, h1, meta, crumbs, projects)
    cards = "\n".join(project_card(row) for row in projects)
    return f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(meta)}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="acre&amp;key">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(meta)}">
  <meta property="og:url" content="{canonical}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(meta)}">
  <link rel="icon" type="image/svg+xml" href="../../../style-guide/assets/favicon.svg">
  <link rel="stylesheet" href="../../../website.min.css?v=20261020_footer_v6">
  <script type="application/ld+json">
{ld}
  </script>
  <style>
    body {{ background:#FAFAFA; color:#55555A; }}
    .hub-main {{ padding: 6.5rem 0 3rem; }}
    .hub-wrap {{ width:min(1120px, calc(100% - 2rem)); margin:0 auto; }}
    .hub-kicker {{ font-family:Manrope,sans-serif; font-size:0.75rem; font-weight:700; letter-spacing:0.14em; text-transform:uppercase; color:#804526; }}
    .hub-main h1 {{ font-family:'Cormorant Garamond',serif; font-weight:400; font-size:clamp(2rem,1.4rem + 1.4vw,2.75rem); color:#2B2D31; margin:0.35rem 0 0.75rem; line-height:1.15; }}
    .hub-grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(260px,1fr)); gap:0.75rem; margin-top:1.25rem; }}
    .page-breadcrumb {{ display:flex; flex-wrap:wrap; gap:0.45rem; list-style:none; padding:0; margin:0 0 1rem; font-family:Manrope,sans-serif; font-size:0.84rem; color:#55555A; }}
    .page-breadcrumb a {{ color:#55555A; text-decoration:none; }}
    .page-breadcrumb a:hover {{ color:#804526; }}
    .page-breadcrumb .current {{ color:#804526; font-weight:600; }}
    @media (max-width: 700px) {{
      .hub-main {{ padding-top: 5.5rem; }}
      .hub-grid {{ grid-template-columns:1fr; }}
    }}
  </style>
</head>
<body>
{header_html}
<main class="hub-main">
  <div class="hub-wrap">
    <nav aria-label="breadcrumb">{crumb_html(crumb_visible)}</nav>
    <p class="hub-kicker">acre&amp;key research</p>
    <h1>{esc(h1)}</h1>
    <p style="{REL}">Updated 23 Oct 2026</p>
    {intro_html}
    {extra_html}
    <div class="hub-grid">
{cards}
    </div>
  </div>
</main>
{footer_html}
<script>window.openModal = window.openModal || function () {{ window.location.href = '/contact/'; }};</script>
<script src="../../../website.min.js?v=20261020_footer_v6" defer></script>
</body>
</html>
"""


def build_hubs(plan: list[dict], hub_rows: list[dict], props: dict, area_of: dict[str, str]) -> list[str]:
    by_area: dict[str, list[str]] = defaultdict(list)
    for slug, area in area_of.items():
        by_area[area].append(slug)
    for slugs in by_area.values():
        slugs.sort(key=lambda slug: props[slug]["name"].lower())

    dev_of: dict[str, list[str]] = defaultdict(list)
    for row in plan:
        if row["source_type"] != "property":
            continue
        if "/property/developer/" not in row["target"]:
            continue
        slug = url_path(row["source"]).strip("/").split("/")[-1]
        dev = url_path(row["target"]).strip("/").split("/")[-1]
        if slug not in dev_of[dev]:
            dev_of[dev].append(slug)
    for slugs in dev_of.values():
        slugs.sort(key=lambda slug: props[slug]["name"].lower())

    zone_area_links: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for row in plan:
        if row["placement"] != "Area list on zone hub":
            continue
        zone = url_path(row["source"]).strip("/").split("/")[-1]
        zone_area_links[zone].append((row["target"], row["anchor"]))

    guides = {}
    labels = {}
    for row in hub_rows:
        path = url_path(row["url"])
        if "/property/" not in path:
            continue
        slug = path.strip("/").split("/")[-1]
        labels[slug] = row["name"]
        found = re.findall(r"/blogs/areas/[a-z0-9-]+/", row.get("note") or "")
        guides[slug] = []
        for guide in found:
            if guide not in guides[slug]:
                guides[slug].append(guide)

    created = []
    area_slugs = [slug for slug in by_area if slug not in ZONE_LABEL]
    for zone, areas in (
        ("east-bengaluru", ["whitefield", "sarjapur-road", "budigere-cross", "kr-puram", "varthur", "panathur"]),
        ("north-bengaluru", ["devanahalli", "bagalur", "yelahanka", "tumkur-road", "thanisandra"]),
        ("south-bengaluru", ["bannerghatta-road", "kanakapura-road", "hosur-road"]),
        ("west-bengaluru", ["mysore-road"]),
    ):
        pass

    # Area hubs
    for area in area_slugs:
        zone = ZONE_OF[area]
        slugs = by_area[area]
        rows = [props[slug] for slug in slugs]
        h1 = labels.get(area, area)
        siblings = [other for other in area_slugs if ZONE_OF[other] == zone and other != area]
        sibling_html = ""
        if siblings:
            links = " · ".join(
                a_tag(f"https://acrenkey.com/property/area/{other}/", labels.get(other, other))
                for other in siblings[:4]
            )
            sibling_html = sentence(f"Other micro-markets in {esc(ZONE_LABEL[zone])}: {links}.")
        guide_bits = [
            a_tag("https://acrenkey.com" + guide, guide_label(guide)) for guide in guides.get(area, [])
        ]
        guide_html = sentence("Area guides: " + " · ".join(guide_bits) + ".") if guide_bits else ""
        place = h1.replace("Property in ", "")
        intro = sentence(
            f"acre&amp;key has reviewed {len(rows)} residential projects in {esc(place)}. "
            f"Each card repeats the configuration, size range, possession timing and Karnataka RERA registration already published on that project page. "
            f"Projects are listed alphabetically. "
            f'See {a_tag("https://acrenkey.com/property/area/" + zone + "/", ZONE_LABEL[zone])} '
            f'or the full {a_tag("https://acrenkey.com/property/", "Properties")} index.'
        )
        crumbs = [
            ("Home", "https://acrenkey.com/"),
            ("Properties", "https://acrenkey.com/property/"),
            (ZONE_LABEL[zone], f"https://acrenkey.com/property/area/{zone}/"),
            (h1, f"https://acrenkey.com/property/area/{area}/"),
        ]
        description = (
            f"Projects acre&key has reviewed in {place}, Bengaluru, with configuration, size, possession and Karnataka RERA numbers from each project page."
        )
        html_page = render_hub("area", area, h1, rows, crumbs, intro + sibling_html + guide_html, "", description)
        dest = ROOT / "property" / "area" / area / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html_page, encoding="utf-8")
        created.append(str(dest.relative_to(ROOT)))

    # Zone hubs, including projects filed directly on the zone.
    for zone in ZONES:
        child_areas = [area for area in area_slugs if ZONE_OF[area] == zone]
        direct = by_area.get(zone, [])
        slugs = []
        for area in child_areas:
            slugs.extend(by_area[area])
        slugs.extend(direct)
        # stable unique
        seen = set()
        ordered = []
        for slug in slugs:
            if slug not in seen:
                seen.add(slug)
                ordered.append(slug)
        ordered.sort(key=lambda slug: props[slug]["name"].lower())
        rows = [props[slug] for slug in ordered]
        h1 = labels.get(zone, ZONE_LABEL[zone])
        area_links = zone_area_links.get(zone, [])
        area_html = sentence(
            "Micro-markets in this zone: "
            + " · ".join(a_tag(url, anchor) for url, anchor in area_links)
            + "."
        )
        other_zones = [other for other in ZONES if other != zone]
        zone_html = sentence(
            "Other zones: "
            + " · ".join(
                a_tag(f"https://acrenkey.com/property/area/{other}/", ZONE_LABEL[other]) for other in other_zones
            )
            + "."
        )
        intro = sentence(
            f"{esc(h1)} lists {len(rows)} residential projects acre&amp;key has reviewed, grouped from the micro-market pages below. "
            f"A project stays on this page when its own page names the zone and not a finer locality. "
            f'Cards repeat configuration, size, possession and Karnataka RERA registration from the project page. '
            f'Start from {a_tag("https://acrenkey.com/property/", "Properties")} to see every Bengaluru project.'
        )
        crumbs = [
            ("Home", "https://acrenkey.com/"),
            ("Properties", "https://acrenkey.com/property/"),
            (h1, f"https://acrenkey.com/property/area/{zone}/"),
        ]
        description = (
            f"{h1} reviewed by acre&key, with each micro-market and the configuration, size, possession and Karnataka RERA number from the project page."
        )
        html_page = render_hub("area", zone, h1, rows, crumbs, intro + area_html + zone_html, "", description)
        dest = ROOT / "property" / "area" / zone / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html_page, encoding="utf-8")
        created.append(str(dest.relative_to(ROOT)))

    dev_labels = {}
    for row in hub_rows:
        path = url_path(row["url"])
        if "/property/developer/" in path:
            dev_labels[path.strip("/").split("/")[-1]] = row["name"]
    dev_slugs = sorted(dev_of)
    for dev in dev_slugs:
        rows = [props[slug] for slug in dev_of[dev]]
        h1 = dev_labels.get(dev, dev.title() + " projects reviewed by acre&key")
        siblings = [other for other in dev_slugs if other != dev][:3]
        sibling_html = sentence(
            "Other developer lists: "
            + " · ".join(
                a_tag(
                    f"https://acrenkey.com/property/developer/{other}/",
                    dev_labels.get(other, other),
                )
                for other in siblings
            )
            + "."
        )
        intro = sentence(
            f"This page lists {len(rows)} {esc(h1.split(' projects')[0])} projects acre&amp;key has reviewed in Bengaluru. "
            f"Each card repeats configuration, size, possession and the Karnataka RERA registration from that project page. "
            f"The list is alphabetical. "
            f'Browse {a_tag("https://acrenkey.com/property/", "Properties")} for the full set.'
        )
        crumbs = [
            ("Home", "https://acrenkey.com/"),
            ("Properties", "https://acrenkey.com/property/"),
            (h1, f"https://acrenkey.com/property/developer/{dev}/"),
        ]
        description = (
            f"{h1}. Configuration, size, possession and Karnataka RERA numbers are copied from each project page."
        )
        html_page = render_hub("developer", dev, h1, rows, crumbs, intro + sibling_html, "", description)
        dest = ROOT / "property" / "developer" / dev / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html_page, encoding="utf-8")
        created.append(str(dest.relative_to(ROOT)))
    return created


def hand_blocks(path: Path, groups: dict[str, list[tuple[str, str]]]) -> list[tuple[int, str]]:
    inserts = []
    page_key = str(path.relative_to(ROOT))
    if page_key == "index.html":
        # Filled by the caller once the page text is known.
        return inserts
    return inserts


def build_page_inserts(page: str, groups: dict[str, list[tuple[str, str]]], rel: str) -> tuple[str, list[str]]:
    inserts: list[tuple[int, str]] = []
    notes: list[str] = []
    used = set()

    def add(key: str, pos: int | None, snippet: str, note: str):
        if pos is None:
            pos = footer_pos(page)
            notes.append(f"{rel}: {key} placed before footer ({note})")
        else:
            notes.append(f"{rel}: {key} in section")
        inserts.append((pos, snippet))
        used.add(key)

    if rel == "index.html":
        hero_bits = []
        if "hero" in groups or "after_hero" in groups:
            parts = []
            if "hero" in groups:
                parts.append(a_tag(*groups["hero"][0]))
            if "after_hero" in groups:
                parts.append(a_tag(*groups["after_hero"][0]))
            if len(parts) == 2:
                hero_bits.append(sentence(f"See {parts[0]}, then {parts[1]}."))
            elif parts:
                hero_bits.append(sentence(f"See {parts[0]}."))
            used.update({"hero", "after_hero"})
        if "learn" in groups:
            links = " and ".join(a_tag(url, anchor) for url, anchor in groups["learn"])
            hero_bits.append(sentence(f"Learn before you buy with {links}."))
            used.add("learn")
        if "explore" in groups:
            links = ", ".join(a_tag(url, anchor) for url, anchor in groups["explore"])
            hero_bits.append(sentence(f"Explore by area: {links}."))
            used.add("explore")
        if hero_bits:
            match = re.search(r"</h1>", page, flags=re.I)
            pos = match.end() if match else footer_pos(page)
            inserts.append((pos, "".join(hero_bits)))
        if "tools" in groups:
            links = ", ".join(a_tag(url, anchor) for url, anchor in groups["tools"])
            inserts.append((footer_pos(page), sentence(f"Tools and guides before you decide: {links}.")))
            used.add("tools")

    if rel == "contact/index.html" and "closing" in groups:
        link = a_tag(*groups["closing"][0])
        pos = placement_pos(page, "closing") or footer_pos(page)
        inserts.append((pos, sentence(f"Read how a {link} works with buyers.")))
        used.add("closing")

    if rel == "property-consultant-bengaluru/index.html":
        if "cta" in groups:
            link = a_tag(*groups["cta"][0])
            pos = placement_pos(page, "cta") or footer_pos(page)
            inserts.append((pos, sentence(f"When you are ready, {link}.")))
            used.add("cta")
        resource_links = []
        if "resources" in groups:
            resource_links.extend(groups["resources"])
            used.add("resources")
        if "faq" in groups:
            resource_links.extend(groups["faq"])
            used.add("faq")
        if resource_links:
            pos = placement_pos(page, "faq") or footer_pos(page)
            body = " and ".join(a_tag(url, anchor) for url, anchor in resource_links)
            inserts.append((pos, sentence(f"Keep reading: {body}.")))

    if rel == "careers/index.html" and "roles" in groups:
        links = ", ".join(a_tag(url, anchor) for url, anchor in groups["roles"])
        pos = placement_pos(page, "roles") or footer_pos(page)
        inserts.append((pos, sentence(f"Open roles: {links}.")))
        used.add("roles")

    if "browse" in groups:
        chips = "".join(
            f'<a href="{esc(href_for(url))}" style="{CHIP}">{esc(anchor)}</a>'
            for url, anchor in groups["browse"]
        )
        block = (
            '<div class="ak-browse-row" data-ak-rel="1" style="margin:1rem 0 0.5rem;">'
            '<p style="font-family:Manrope,sans-serif;font-size:0.78rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#804526;margin:0 0 0.45rem;">Browse by area and developer</p>'
            f"{chips}</div>"
        )
        match = re.search(r'<p class="props-subtitle">.*?</p>', page, flags=re.S)
        pos = match.end() if match else footer_pos(page)
        inserts.append((pos, block))
        used.add("browse")

    lead = {
        "developer": "Developer page",
        "faq": "Related questions",
        "price_emi": "Before you shortlist",
        "price_stamp": "Registration cost",
        "floor": "Layout check",
        "similar": "More homes nearby",
        "investment": "Return context",
        "location": "Micro-market reading",
        "how": "How this fits",
        "next": "Next calculators",
        "results": "Next step",
    }
    for key, links in groups.items():
        if key in used or key in ("nav", "breadcrumb", "areas"):
            continue
        pos = placement_pos(page, key)
        label = lead.get(key, "Related")
        if key.startswith("sec:"):
            label = "Related"
        snippet = related(links, label)
        if pos is None:
            pos = footer_pos(page)
            notes.append(f"{rel}: {key} before footer")
        inserts.append((pos, snippet))
    return apply_inserts(page, inserts), notes


def update_sitemap(paths: list[str]) -> int:
    sitemap = ROOT / "sitemap.xml"
    text = sitemap.read_text(encoding="utf-8")
    added = 0
    block = []
    for path in paths:
        loc = "https://acrenkey.com/" + path.split("index.html")[0].replace("\\", "/")
        if not loc.endswith("/"):
            loc += "/"
        if loc in text:
            continue
        block.append(
            "  <url>\n"
            f"    <loc>{loc}</loc>\n"
            "    <lastmod>2026-10-23</lastmod>\n"
            "    <changefreq>weekly</changefreq>\n"
            "    <priority>0.8</priority>\n"
            "  </url>\n"
        )
        added += 1
    if block:
        text = text.replace("</urlset>", "".join(block) + "</urlset>")
        sitemap.write_text(text, encoding="utf-8")
    return added


def main() -> None:
    plan = load_csv(PLAN)
    hub_rows = load_csv(HUBS)
    props = load_properties()
    area_anchor = {}
    area_of = {}
    for row in plan:
        if row["source_type"] == "property" and row["placement"] == "Breadcrumb":
            slug = url_path(row["source"]).strip("/").split("/")[-1]
            area = url_path(row["target"]).strip("/").split("/")[-1]
            area_anchor[slug] = (area, row["anchor"])
            area_of[slug] = area

    created = build_hubs(plan, hub_rows, props, area_of)
    print(f"hubs created: {len(created)}")

    grouped: dict[Path, dict[str, list[tuple[str, str]]]] = defaultdict(lambda: defaultdict(list))
    missing_sources = []
    skipped = []
    for row in plan:
        if "/partners" in row["target"] or row["target"].endswith("partners.html"):
            skipped.append((row["source"], row["target"], row["anchor"], "partners page removed on this branch"))
            continue
        path = source_file(row["source"])
        if path is None:
            missing_sources.append(row)
            skipped.append((row["source"], row["target"], row["anchor"], "source page is not in this repo"))
            continue
        key = bucket(row["placement"])
        if key == "areas":
            # Baked into the zone hub.
            continue
        if key == "nav":
            continue
        if key == "breadcrumb":
            continue
        grouped[path][key].append((row["target"], row["anchor"]))

    notes = []
    for path, groups in grouped.items():
        original = path.read_text(encoding="utf-8")
        updated, page_notes = build_page_inserts(original, groups, str(path.relative_to(ROOT)))
        notes.extend(page_notes)
        if "/property/" in str(path) and path.parent.name not in ("area", "developer", "property"):
            slug = path.parent.name
            if slug in area_anchor and path.parent.parent.name == "property":
                updated = update_project_breadcrumb(updated, slug, props, area_anchor)
        path.write_text(updated, encoding="utf-8")

    html_files = [path for path in ROOT.rglob("*.html") if "style-guide" not in path.parts]
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        text = replace_desktop_nav(text)
        text = replace_mobile_nav(text)
        text = replace_footer_nav(text)
        text = fix_href_hygiene(text)
        text = compliance_phrases(text)
        text = rewrite_visible(text)
        path.write_text(text, encoding="utf-8")

    added = update_sitemap(created)
    report = {
        "hubs": created,
        "sitemap_added": added,
        "skipped": skipped,
        "missing_sources": len(missing_sources),
        "fallback_notes": [note for note in notes if "before footer" in note],
    }
    (ROOT / "scripts" / "link-apply-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"skipped {len(skipped)} missing_sources {len(missing_sources)} sitemap_added {added}")
    print(f"fallback notes {len(report['fallback_notes'])}")
    for note in report["fallback_notes"][:40]:
        print(" ", note)


if __name__ == "__main__":
    main()
