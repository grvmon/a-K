#!/usr/bin/env python3
"""Close remaining internal-link, footer, title and markup gaps.

Does not re-run apply_internal_links.py. Safe to run once on the edited tree.
"""

from __future__ import annotations

import html as html_lib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify_internal_links as verify

ROOT = verify.ROOT

FOOTER_NAV = """      <nav class="ak-footer-links" aria-label="Footer">
        <a href="/property/">Properties</a>
        <a href="/property/area/east-bengaluru/">East Bengaluru</a>
        <a href="/property/area/north-bengaluru/">North Bengaluru</a>
        <a href="/property/area/south-bengaluru/">South Bengaluru</a>
        <a href="/property/area/west-bengaluru/">West Bengaluru</a>
        <a href="/calculators/">Calculators</a>
        <a href="https://acrenkey.com/blogs/">Blog</a>
        <a href="https://answers.acrenkey.com/">Answers</a>
        <a href="/">Home</a>
        <a href="/property-consultant-bengaluru/">Property Consultant in Bengaluru</a>
        <a href="/careers/">Careers</a>
        <a href="/contact/">Contact</a>
        <a href="/privacy-policy/">Privacy Policy</a>
        <a href="/terms-of-service/">Terms of Service</a>
        <a href="/rera-disclaimer/">RERA Disclaimer</a>
      </nav>
"""

LINK_ATTR = 'style="color:#804526;text-decoration:underline;text-underline-offset:3px;"'
P_ATTR = (
    'class="ak-inline-related" data-ak-topup="1" '
    'style="font-family:Manrope,sans-serif;font-size:0.95rem;line-height:1.6;'
    'color:#55555A;margin:0.85rem 0 1.1rem;"'
)

STRAY_FOOTER = re.compile(
    r"</footer>\s*</div>\s*<!-- Bottom Bar -->.*?</footer>",
    re.S,
)


def esc(text: str) -> str:
    return html_lib.escape(text, quote=True)


def load_pages():
    pages = {}
    for path in verify.html_files():
        pages[path] = path.read_text(encoding="utf-8", errors="replace")
    return pages


def content_index(pages):
    url_of = {}
    rel_of = {}
    for path, text in pages.items():
        if not verify.is_content(path):
            continue
        rel = str(path.relative_to(ROOT))
        url = "/" if rel == "index.html" else "/" + rel[: -len("index.html")]
        url_of[url] = path
        rel_of[url] = rel
    return url_of, rel_of


def referrers_for(pages, url_of):
    referrers = defaultdict(set)
    for path, page in pages.items():
        base = verify.page_base(path)
        body = verify.main_slice(page)
        rel = str(path.relative_to(ROOT))
        for href, _text, _pos in verify.extract_anchors(body):
            local = verify.local_target(href, base)
            if local in url_of and url_of[local] != path:
                referrers[local].add(rel)
    return referrers


def h1_text(page: str, fallback: str) -> str:
    match = re.search(r"(?is)<h1\b[^>]*>(.*?)</h1>", page)
    raw = match.group(1) if match else fallback
    text = re.sub(r"(?is)<[^>]+>", " ", raw)
    text = " ".join(html_lib.unescape(text).split())
    text = re.sub(r"\s*\|\s*acre&key.*$", "", text, flags=re.I)
    text = re.sub(
        r"\b(?:best|luxury|premium|guaranteed|independent|objective|unbiased)\b",
        "",
        text,
        flags=re.I,
    )
    text = " ".join(text.split())
    if len(text) > 80:
        text = text[:77].rsplit(" ", 1)[0]
    return text or fallback


def link_html(href: str, anchor: str) -> str:
    return f'<a href="{esc(href)}" {LINK_ATTR}>{esc(anchor)}</a>'


def sentence(lead: str, links: list[tuple[str, str]]) -> str:
    parts = [link_html(href, anchor) for href, anchor in links]
    if len(parts) == 1:
        joined = parts[0]
    elif len(parts) == 2:
        joined = f"{parts[0]} and {parts[1]}"
    else:
        joined = ", ".join(parts[:-1]) + " and " + parts[-1]
    return f"<p {P_ATTR}>{lead} {joined}.</p>"


def insert_before_footer(page: str, block: str) -> str:
    match = re.search(r"(?i)<footer\b", page)
    if not match:
        match = re.search(r"(?i)</body>", page)
    if not match:
        return page + block
    return page[: match.start()] + block + "\n" + page[match.start() :]


def inject_footer(page: str) -> str:
    if "ak-footer-links" in page or "ak-footer-bottom" not in page:
        return page
    return page.replace('<div class="ak-footer-bottom">', FOOTER_NAV + '    <div class="ak-footer-bottom">', 1)


def project_links(page: str) -> list[str]:
    found = re.findall(r'href="(/property/[a-z0-9-]+/)"', page)
    unique = []
    for href in found:
        if href not in unique:
            unique.append(href)
    return unique


def choose_title(label: str, kind: str) -> str:
    brand = " | acre&key"
    if kind == "zone":
        options = [
            f"Reviewed {label} property projects{brand}",
            f"Reviewed projects in {label}{brand}",
            f"{label} property projects{brand}",
        ]
    elif kind == "developer":
        options = [
            f"Reviewed {label} projects across Bengaluru{brand}",
            f"{label} projects reviewed in Bengaluru{brand}",
            f"Reviewed {label} projects in Bengaluru{brand}",
            f"{label} projects in Bengaluru{brand}",
            f"{label} projects we have reviewed{brand}",
        ]
    else:
        short = label.split(" / ")[0]
        options = [
            f"Reviewed {label} projects in Bengaluru{brand}",
            f"Reviewed projects in {label}, Bengaluru{brand}",
            f"{label} projects reviewed in Bengaluru{brand}",
            f"Reviewed {short} projects in Bengaluru{brand}",
            f"{label} projects in Bengaluru{brand}",
            f"Reviewed projects in {short}, Bengaluru{brand}",
        ]
    fitting = [item for item in options if 50 <= len(item) <= 60]
    if fitting:
        return sorted(fitting, key=lambda item: abs(len(item) - 55))[0]
    under = [item for item in options if len(item) <= 60]
    if under:
        return max(under, key=len)
    return min(options, key=len)


def choose_description(label: str, kind: str) -> str:
    if kind == "zone":
        text = (
            f"{label} projects reviewed by acre&key, with each micro-market and the "
            "configuration, size, possession and Karnataka RERA number from the project page."
        )
    elif kind == "developer":
        text = (
            f"{label} projects reviewed by acre&key in Bengaluru. Each card lists "
            "configuration, size, possession and the Karnataka RERA number from that project page."
        )
    else:
        text = (
            f"Projects acre&key has reviewed in {label}, Bengaluru, with configuration, "
            "size, possession and the Karnataka RERA number from each project page."
        )
    if len(text) > 160:
        short = label.split(" / ")[0]
        text = (
            f"Projects acre&key has reviewed in {short}, Bengaluru. Cards list "
            "configuration, size, possession and the Karnataka RERA number."
        )
    if len(text) < 140:
        extra = " No price is listed."
        if len(text.rstrip(".") + "." + extra) <= 160:
            text = text.rstrip(".") + "." + extra
    return text


def replace_meta_content(page: str, attr_pattern: str, value: str) -> str:
    escaped = esc(value)

    def repl(match: re.Match) -> str:
        tag = match.group(0)
        if not re.search(attr_pattern, tag, flags=re.I):
            return tag
        return re.sub(r'content="[^"]*"', f'content="{escaped}"', tag, count=1)

    return re.sub(r"<meta\b[^>]*>", repl, page)


def retitle_hubs(pages) -> list[str]:
    notes = []
    for path, page in list(pages.items()):
        rel = str(path.relative_to(ROOT))
        if not (rel.startswith("property/area/") or rel.startswith("property/developer/")):
            continue
        kind = "developer" if "/developer/" in rel else "area"
        if rel.startswith("property/area/") and rel.split("/")[2].endswith("-bengaluru"):
            kind = "zone"
        h1 = h1_text(page, "Bengaluru")
        if kind == "zone":
            label = h1.replace(" projects", "").strip()
        elif kind == "developer":
            label = re.sub(r"\s+projects.*$", "", h1).strip()
        else:
            label = re.sub(r"^Property in\s+", "", h1).strip()
        title = choose_title(label, kind)
        description = choose_description(label, kind)
        page = re.sub(r"<title>.*?</title>", f"<title>{esc(title)}</title>", page, count=1, flags=re.S)
        page = replace_meta_content(page, r"og:title|twitter:title", title)
        page = replace_meta_content(page, r'name="description"|og:description|twitter:description', description)
        json_desc = description.replace("&", "&")
        page = re.sub(
            r'("description":\s*")([^"]*)(")',
            lambda match, text=json_desc: match.group(1) + text.replace("\\", "\\\\").replace('"', '\\"') + match.group(3),
            page,
            count=1,
        )
        pages[path] = page
        notes.append(f"{rel} title={len(title)} {title} desc={len(description)}")
    return notes


def markup_fixes(pages) -> list[str]:
    notes = []
    home = ROOT / "index.html"
    if home in pages:
        pages[home] = re.sub(r"\bpremiums\b", "mark-ups", pages[home])
        notes.append("home: premiums -> mark-ups")

    folium = ROOT / "property/sumadhura-folium-whitefield/index.html"
    if folium in pages and "</main>" in pages[folium]:
        pages[folium] = pages[folium].replace("</main>", "</div>\n</main>", 1)
        notes.append("folium: closed the open div before </main>")

    template = ROOT / "property-template.html"
    if template in pages:
        text = pages[template]
        text = text.replace("https://acrenkey.com/bengaluru/east-bengaluru/", "https://acrenkey.com/property/area/east-bengaluru/")
        text = text.replace("https://acrenkey.com/bengaluru/varthur/", "https://acrenkey.com/property/area/varthur/")
        text = text.replace("https://acrenkey.com/bengaluru/", "https://acrenkey.com/property/")
        text = text.replace('href="/bengaluru/east-bengaluru/"', 'href="/property/area/east-bengaluru/"')
        text = text.replace('href="/bengaluru/varthur/"', 'href="/property/area/varthur/"')
        text = text.replace('href="/bengaluru/"', 'href="/property/"')
        text = text.replace(">Bengaluru</a>", ">Properties</a>")
        pages[template] = text
        notes.append("property-template: breadcrumb points at property hubs")

    for path, page in list(pages.items()):
        updated = inject_footer(page)
        if updated != page:
            pages[path] = updated
            notes.append("footer nav: " + str(path.relative_to(ROOT)))
        cleaned, count = STRAY_FOOTER.subn("</footer>", pages[path], count=1)
        if count:
            pages[path] = cleaned
            notes.append("removed stray footer: " + str(path.relative_to(ROOT)))
    return notes


def kind_of(url: str) -> str:
    if url == "/calculators/" or url.startswith("/calculators/"):
        return "calculator"
    if url.startswith("/property/area/") and url.rstrip("/").endswith("-bengaluru"):
        return "zone"
    if url.startswith("/property/area/"):
        return "area"
    if url.startswith("/property/developer/"):
        return "developer"
    if url.startswith("/property/") and url != "/property/":
        return "project"
    return "site"


def assign_links(pages, url_of, rel_of):
    """Return donor rel -> list of (lead, links)."""
    referrers = referrers_for(pages, url_of)
    need = {}
    for url, rel in rel_of.items():
        if rel.startswith(("privacy-policy/", "terms-of-service/", "rera-disclaimer/")):
            continue
        deficit = 5 - len(referrers[url])
        if deficit > 0:
            need[url] = deficit

    assignments = defaultdict(list)  # donor rel -> list[(href, anchor)]
    donor_count = defaultdict(int)
    planned = defaultdict(set)  # donor rel -> urls

    def linked(donor_rel: str, url: str) -> bool:
        return donor_rel in referrers[url] or url in planned[donor_rel]

    def give(donor_rel: str, url: str, anchor: str) -> bool:
        if donor_rel not in rel_of.values():
            return False
        if url not in need or need[url] <= 0:
            return False
        if donor_rel == rel_of[url] or linked(donor_rel, url):
            return False
        if donor_count[donor_rel] >= 6:
            return False
        assignments[donor_rel].append((url, anchor))
        planned[donor_rel].add(url)
        donor_count[donor_rel] += 1
        need[url] -= 1
        referrers[url].add(donor_rel)
        return True

    def anchor_for(url: str) -> str:
        return h1_text(pages[url_of[url]], url.strip("/").replace("-", " "))

    # Site pages: short, specific cross-links.
    site_plan = {
        "index.html": [
            ("/contact/", "Contact acre&key"),
            ("/careers/", "Careers at acre&key"),
            ("/careers/home-buyer-advisor/", "Home buyer advisor role"),
            ("/careers/property-consultant-inside-sales/", "Property consultant role"),
            ("/careers/executive-assistant-to-the-founder/", "Executive assistant role"),
            ("/property-consultant-bengaluru/", "Property Consultant in Bengaluru"),
            ("/calculators/", "acre&key calculators"),
        ],
        "contact/index.html": [
            ("/", "acre&key home"),
            ("/careers/", "Careers at acre&key"),
            ("/careers/home-buyer-advisor/", "Home buyer advisor role"),
            ("/careers/property-consultant-inside-sales/", "Property consultant role"),
            ("/careers/executive-assistant-to-the-founder/", "Executive assistant role"),
            ("/property-consultant-bengaluru/", "Property Consultant in Bengaluru"),
            ("/property/", "reviewed Bengaluru properties"),
            ("/calculators/", "acre&key calculators"),
        ],
        "careers/index.html": [
            ("/", "acre&key home"),
            ("/contact/", "Contact acre&key"),
            ("/property-consultant-bengaluru/", "Property Consultant in Bengaluru"),
        ],
        "property-consultant-bengaluru/index.html": [
            ("/", "acre&key home"),
            ("/contact/", "Contact acre&key"),
            ("/careers/", "Careers at acre&key"),
            ("/property/", "reviewed Bengaluru properties"),
            ("/calculators/", "acre&key calculators"),
        ],
        "calculators/index.html": [],
        "property/index.html": [
            ("/", "acre&key home"),
            ("/contact/", "Contact acre&key"),
            ("/property-consultant-bengaluru/", "Property Consultant in Bengaluru"),
        ],
    }
    role_pages = [
        "careers/home-buyer-advisor/index.html",
        "careers/property-consultant-inside-sales/index.html",
        "careers/executive-assistant-to-the-founder/index.html",
    ]
    for rel in role_pages:
        others = [item for item in role_pages if item != rel]
        site_plan[rel] = [("/", "acre&key home"), ("/contact/", "Contact acre&key"), ("/careers/", "Careers at acre&key")]
        for other in others:
            url = "/" + other[: -len("index.html")]
            site_plan[rel].append((url, anchor_for(url)))

    for donor_rel, links in site_plan.items():
        for href, anchor in links:
            give(donor_rel, href, anchor)

    # Weak area and developer hubs get a body link from their own project pages.
    for url, rel in list(rel_of.items()):
        if kind_of(url) not in ("area", "developer", "zone"):
            continue
        if url not in need or need[url] <= 0:
            continue
        projects = project_links(pages[url_of[url]])
        label = anchor_for(url)
        for project in projects:
            if need.get(url, 0) <= 0:
                break
            donor_rel = rel_of.get(project)
            if not donor_rel:
                continue
            give(donor_rel, url, label)

    # Weak projects: two siblings from the same area hub, then the property index.
    area_projects = {}
    for url in rel_of:
        if kind_of(url) != "area":
            continue
        area_projects[url] = project_links(pages[url_of[url]])
    for url in list(need):
        if kind_of(url) != "project" or need[url] <= 0:
            continue
        siblings = []
        for projects in area_projects.values():
            if url in projects:
                siblings = [item for item in projects if item != url]
                break
        for sibling in siblings:
            if need[url] <= 0:
                break
            donor_rel = rel_of.get(sibling)
            if donor_rel:
                give(donor_rel, url, anchor_for(url))
        if need[url] > 0:
            give("property/index.html", url, anchor_for(url))
        if need[url] > 0:
            give("calculators/index.html", url, anchor_for(url))

    # Calculators and anything still short: round-robin across the same section.
    calc_donors = sorted(rel for url, rel in rel_of.items() if url.startswith("/calculators/") and url != "/calculators/")
    cursor = 0
    still = [url for url, deficit in need.items() if deficit > 0 and kind_of(url) == "calculator"]
    for index, url in enumerate(still):
        while need[url] > 0:
            if not calc_donors:
                break
            donor_rel = calc_donors[cursor % len(calc_donors)]
            cursor += 1
            if cursor > len(calc_donors) * 8:
                break
            before = need[url]
            give(donor_rel, url, anchor_for(url))
            if need[url] == before and cursor > len(calc_donors) * 2 and donor_count[donor_rel] >= 6:
                continue
            if need[url] == before and all(donor_count[item] >= 6 or linked(item, url) or item == rel_of[url] for item in calc_donors):
                break
        # Hub link so /calculators/ itself reaches 5 in-text referrers.
        if need.get("/calculators/", 0) > 0:
            give(rel_of[url], "/calculators/", "acre&key calculators")

    # Last pass for hubs and site pages that are still short.
    property_donors = [rel for url, rel in rel_of.items() if url.startswith("/property/") and url != "/property/"]
    cursor = 0
    for url in list(need):
        guard = 0
        while need[url] > 0 and guard < 400:
            guard += 1
            pool = calc_donors if kind_of(url) == "calculator" else property_donors
            if not pool:
                break
            donor_rel = pool[cursor % len(pool)]
            cursor += 1
            before = need[url]
            give(donor_rel, url, anchor_for(url))
            if need[url] == before and guard > len(pool):
                # Relax the per-donor cap for the last few links.
                if donor_count[donor_rel] < 10 and not linked(donor_rel, url) and donor_rel != rel_of[url]:
                    donor_count[donor_rel] = min(donor_count[donor_rel], 5)
                    give(donor_rel, url, anchor_for(url))
                if need[url] == before:
                    break
    return assignments, need


def apply_assignments(pages, assignments, rel_of):
    by_donor = assignments
    inverse = {rel: url for url, rel in rel_of.items()}
    for donor_rel, links in by_donor.items():
        path = ROOT / donor_rel
        if path not in pages or not links:
            continue
        donor_url = inverse.get(donor_rel, "")
        if donor_url.startswith("/calculators/"):
            lead = "Related calculators:"
        elif donor_url.startswith("/property/"):
            lead = "Also reviewed:"
        elif donor_rel.startswith("careers/"):
            lead = "Elsewhere at acre&amp;key:"
        else:
            lead = "Elsewhere at acre&amp;key:"
        block = sentence(lead, links)
        pages[path] = insert_before_footer(pages[path], block)


def main() -> int:
    pages = load_pages()
    notes = markup_fixes(pages)
    notes.extend(retitle_hubs(pages))
    url_of, rel_of = content_index(pages)
    assignments, remaining = assign_links(pages, url_of, rel_of)
    apply_assignments(pages, assignments, rel_of)
    added = sum(len(links) for links in assignments.values())
    for path, text in pages.items():
        path.write_text(text, encoding="utf-8")
    report = {
        "links_added": added,
        "donors": len(assignments),
        "still_short": {url: count for url, count in remaining.items() if count > 0},
        "notes_sample": notes[:80],
        "footer_notes": sum(1 for note in notes if note.startswith("footer")),
        "title_notes": [note for note in notes if " title=" in note],
    }
    out = ROOT / "scripts" / "link-finish-report.json"
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({"links_added": added, "donors": len(assignments), "still_short": report["still_short"], "footer_notes": report["footer_notes"]}, indent=2))
    print("titles:")
    for note in report["title_notes"]:
        print(" ", note)
    return 0


if __name__ == "__main__":
    sys.exit(main())
