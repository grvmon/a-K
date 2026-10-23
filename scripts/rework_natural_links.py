#!/usr/bin/env python3
"""Replace stuffed keyword links with one short related block per page.

Removes the machine-inserted related paragraphs, restores the home hero
structure, and adds at most one nearby/related list (3-6 items) plus a
few single-sentence links on calculator pages.
"""

from __future__ import annotations

import csv
import html as html_lib
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify_internal_links as verify

ROOT = verify.ROOT
PLAN = Path("/home/ubuntu/.cursor/projects/workspace/uploads/link_plan_aK_2db7.csv")

ZONES = {
    "east-bengaluru": ["whitefield", "sarjapur-road", "budigere-cross", "kr-puram", "varthur", "panathur"],
    "north-bengaluru": ["devanahalli", "bagalur", "yelahanka", "tumkur-road", "thanisandra"],
    "south-bengaluru": ["bannerghatta-road", "kanakapura-road", "hosur-road"],
    "west-bengaluru": ["mysore-road"],
}
AREA_ZONE = {area: zone for zone, areas in ZONES.items() for area in areas}
AREA_LABEL = {
    "whitefield": "Whitefield",
    "sarjapur-road": "Sarjapur Road",
    "budigere-cross": "Budigere Cross",
    "kr-puram": "KR Puram",
    "varthur": "Varthur",
    "panathur": "Panathur",
    "devanahalli": "Devanahalli",
    "bagalur": "Bagalur",
    "yelahanka": "Yelahanka",
    "tumkur-road": "Tumkur Road",
    "thanisandra": "Thanisandra",
    "bannerghatta-road": "Bannerghatta Road",
    "kanakapura-road": "Kanakapura Road",
    "hosur-road": "Hosur Road",
    "mysore-road": "Mysore Road",
    "east-bengaluru": "East Bengaluru",
    "north-bengaluru": "North Bengaluru",
    "south-bengaluru": "South Bengaluru",
    "west-bengaluru": "West Bengaluru",
}
DEV_LABEL = {
    "arvind": "Arvind",
    "brigade": "Brigade",
    "casagrand": "Casagrand",
    "godrej": "Godrej",
    "lodha": "Lodha",
    "prestige": "Prestige",
    "puravankara": "Puravankara",
    "ramky": "Ramky",
    "sattva": "Sattva",
    "sobha": "Sobha",
    "sumadhura": "Sumadhura",
}

LINK = 'style="color:#804526;text-decoration:underline;text-underline-offset:3px;"'

# One sentence, one link, on a page that already discusses the topic.
CALC_SENTENCES = {
    "calculators/property-appreciation-calculator/index.html": (
        "A resale figure further out is what the future value calculator works out.",
        "/calculators/future-property-value-calculator/",
        "future value calculator",
    ),
    "calculators/cagr-calculator/index.html": (
        "For a date further out, use the future value calculator.",
        "/calculators/future-property-value-calculator/",
        "future value calculator",
    ),
    "calculators/home-affordability-calculator/index.html": (
        "A larger household budget fits the HNI affordability calculator.",
        "/calculators/hni-home-affordability-calculator/",
        "HNI affordability calculator",
    ),
    "calculators/loan-eligibility-calculator/index.html": (
        "Households with higher income can use the HNI affordability calculator.",
        "/calculators/hni-home-affordability-calculator/",
        "HNI affordability calculator",
    ),
    "calculators/fd-vs-property-calculator/index.html": (
        "A flat near the airport belongs in the north Bengaluru calculator.",
        "/calculators/north-bangalore-investment-calculator/",
        "north Bengaluru calculator",
    ),
    "calculators/leveraged-property-return-calculator/index.html": (
        "A plot near the airport fits the north Bengaluru calculator.",
        "/calculators/north-bangalore-investment-calculator/",
        "north Bengaluru calculator",
    ),
    "calculators/interior-cost-calculator/index.html": (
        "A parking slot is priced in the parking cost calculator.",
        "/calculators/parking-cost-calculator/",
        "parking cost calculator",
    ),
    "calculators/renovation-cost-calculator/index.html": (
        "An extra garage sits in the parking cost calculator.",
        "/calculators/parking-cost-calculator/",
        "parking cost calculator",
    ),
    "calculators/rental-yield-calculator/index.html": (
        "Set that yield beside another asset with the ROI comparison.",
        "/calculators/roi-comparison-calculator/",
        "ROI comparison",
    ),
    "calculators/sip-vs-real-estate-calculator/index.html": (
        "The ROI comparison puts the flat next to another asset.",
        "/calculators/roi-comparison-calculator/",
        "ROI comparison",
    ),
    "calculators/interior-budget-calculator/index.html": (
        "The move itself is in the moving cost calculator.",
        "/calculators/moving-cost-calculator/",
        "moving cost calculator",
    ),
    "calculators/rent-vs-buy-calculator/index.html": (
        "A late handover changes the comparison in the possession delay calculator.",
        "/calculators/possession-delay-cost-calculator/",
        "possession delay calculator",
    ),
    "calculators/ready-to-move-vs-under-construction-calculator/index.html": (
        "Delay risk is what the possession delay calculator totals.",
        "/calculators/possession-delay-cost-calculator/",
        "possession delay calculator",
    ),
    "calculators/should-i-buy-this-property-calculator/index.html": (
        "Carry the visit checklist on the day you see the flat.",
        "/calculators/property-visit-checklist-score/",
        "visit checklist",
    ),
    "calculators/home-buying-readiness-score/index.html": (
        "Take the visit checklist when you walk the site.",
        "/calculators/property-visit-checklist-score/",
        "visit checklist",
    ),
    "calculators/bangalore-property-buying-cost-calculator/index.html": (
        "A Whitefield flat can use the Whitefield cost calculator.",
        "/calculators/whitefield-property-cost-calculator/",
        "Whitefield cost calculator",
    ),
    "calculators/gst-on-property-calculator/index.html": (
        "Whitefield buyers often continue in the Whitefield cost calculator.",
        "/calculators/whitefield-property-cost-calculator/",
        "Whitefield cost calculator",
    ),
    "calculators/net-rental-yield-calculator/index.html": (
        "See when rent covers the holding cost in the break-even calculator.",
        "/calculators/break-even-calculator/",
        "break-even calculator",
    ),
    "calculators/construction-cost-calculator/index.html": (
        "Brick quantities sit in the brick calculator.",
        "/calculators/brick-calculator/",
        "brick calculator",
    ),
    "calculators/builder-trust-score-calculator/index.html": (
        "Set two builders side by side in the builder comparison.",
        "/calculators/builder-comparison-tool/",
        "builder comparison",
    ),
    "calculators/house-hunting-budget-planner/index.html": (
        "The dates for your search sit in the buying timeline.",
        "/calculators/home-buying-timeline-planner/",
        "buying timeline",
    ),
    "calculators/home-loan-prepayment-savings-calculator/index.html": (
        "A shift to another lender uses the balance transfer calculator.",
        "/calculators/home-loan-balance-transfer-calculator/",
        "balance transfer calculator",
    ),
    "calculators/property-comparison-calculator/index.html": (
        "What a lower quote saves is in the negotiation calculator.",
        "/calculators/property-negotiation-savings-calculator/",
        "negotiation calculator",
    ),
    "calculators/section-24-tax-benefit-calculator/index.html": (
        "The yearly municipal levy sits in the property tax calculator.",
        "/calculators/property-tax-calculator/",
        "property tax calculator",
    ),
    "calculators/home-loan-tax-benefit-calculator/index.html": (
        "Principal repayment relief sits in the Section 80C calculator.",
        "/calculators/section-80c-tax-savings-calculator/",
        "Section 80C calculator",
    ),
    "calculators/cement-calculator/index.html": (
        "Steel quantities sit in the steel calculator.",
        "/calculators/steel-calculator/",
        "steel calculator",
    ),
}


def esc(text: str) -> str:
    return html_lib.escape(text, quote=True)


def words(text: str) -> int:
    return len(text.split())


def strip_inserted(page: str) -> str:
    page = re.sub(r'<p class="ak-inline-related".*?</p>', "", page, flags=re.S)
    page = re.sub(r'<div class="ak-browse-row".*?</div>', "", page, flags=re.S)
    page = re.sub(r'<section class="ak-related-reading".*?</section>', "", page, flags=re.S)
    return page


def restore_home_hero(page: str) -> str:
    main = subprocess.check_output(["git", "show", "main:index.html"], text=True, errors="replace")
    start = main.find('<div class="hero-kicker')
    end = main.find("</section>", start)
    original = main[start:end]
    subtitle = (
        '<p class="hero-subtitle premium-subtitle">As a buyer-first '
        "<strong>property consultant in Bangalore</strong>, we help you evaluate properties, "
        "identify risks, and negotiate a sound deal.</p>"
    )
    original = re.sub(
        r'<p class="hero-subtitle premium-subtitle">.*?</p>',
        subtitle,
        original,
        count=1,
        flags=re.S,
    )
    cur_start = page.find('<div class="hero-kicker')
    cur_end = page.find("</section>", cur_start)
    if cur_start < 0 or cur_end < 0 or start < 0:
        raise SystemExit("home hero markers missing")
    return page[:cur_start] + original + page[cur_end:]


def short_project(name: str) -> str:
    original = name
    trimmed = re.sub(r"\s+at\s+.*$", "", name)
    trimmed = re.sub(r"\s+by\s+.*$", "", trimmed)
    # Keep the full name when the short form would be a single word.
    if len(trimmed.split()) < 2:
        trimmed = original
    parts = trimmed.split()
    if len(parts) > 5:
        trimmed = " ".join(parts[:4])
    return trimmed


def place_anchor(slug: str) -> str:
    label = AREA_LABEL[slug]
    if slug.endswith("-bengaluru"):
        return label
    phrase = f"{label} projects"
    if words(phrase) > 5:
        return label
    return phrase


def load_projects() -> dict[str, str]:
    text = (ROOT / "property/properties-data.js").read_text(encoding="utf-8")
    names = {}
    for slug, name in re.findall(r'"slug": "(.*?)".*?"name": "(.*?)"', text, flags=re.S):
        names[slug] = short_project(name)
    return names


def projects_on(page: str) -> list[str]:
    found = re.findall(r'href="(/property/[a-z0-9-]+/)"', page)
    slugs = []
    for href in found:
        slug = href.strip("/").split("/")[-1]
        if slug in ("property",) or href.startswith("/property/area/") or href.startswith("/property/developer/"):
            continue
        if slug not in slugs:
            slugs.append(slug)
    return slugs


def link_item(href: str, anchor: str) -> str:
    if not 2 <= words(anchor) <= 5:
        raise SystemExit(f"anchor length {words(anchor)}: {anchor}")
    return (
        '<li style="border:0.5px solid rgba(85,85,90,0.2);border-radius:4px;background:#FAFAFA;">'
        f'<a href="{esc(href)}" style="display:block;padding:0.7rem 0.9rem;color:#2B2D31;'
        f'text-decoration:none;font-family:Manrope,sans-serif;font-size:0.95rem;">{esc(anchor)}</a>'
        "</li>"
    )


def related_block(title: str, items: list[tuple[str, str]]) -> str:
    seen = set()
    unique = []
    for href, anchor in items:
        if href in seen:
            continue
        seen.add(href)
        unique.append((href, anchor))
    items = unique[:6]
    if len(items) < 3:
        raise SystemExit(f"related block {title} has {len(items)} items")
    lis = "".join(link_item(href, anchor) for href, anchor in items)
    return (
        '<section class="ak-related-reading" aria-labelledby="ak-related-heading" '
        'style="margin:2.5rem auto 1rem;max-width:760px;padding:0 1.25rem;">'
        f'<h2 id="ak-related-heading" style="font-family:\'Cormorant Garamond\',serif;font-weight:400;'
        f'font-size:1.75rem;color:#2B2D31;margin:0 0 0.75rem;">{esc(title)}</h2>'
        f'<ul style="list-style:none;margin:0;padding:0;display:grid;gap:0.5rem;">{lis}</ul>'
        "</section>\n"
    )


def insert_before_footer(page: str, block: str) -> str:
    match = re.search(r"(?i)<footer\b", page)
    if not match:
        raise SystemExit("no footer")
    return page[: match.start()] + block + page[match.start() :]


def hub_intro(kind: str, place: str, count: int) -> str:
    if count <= 0:
        sentence = (
            f"Project cards for {esc(place)} appear here once a dossier is published. "
            "Each card will list the configuration, size, possession and Karnataka RERA number."
        )
    elif kind == "developer":
        sentence = (
            f"acre&amp;key has reviewed {count} residential projects by {esc(place)}. "
            "Each card lists the configuration, size, possession and Karnataka RERA number from that project page."
        )
    else:
        sentence = (
            f"acre&amp;key has reviewed {count} residential projects in {esc(place)}. "
            "Each card lists the configuration, size, possession and Karnataka RERA number from that project page."
        )
    return (
        '<p class="hub-intro" style="font-family:Manrope,sans-serif;font-size:1rem;line-height:1.6;'
        f'color:#55555A;margin:0 0 1.25rem;">{sentence}</p>'
    )


def sentence_html(text: str, href: str, anchor: str) -> str:
    if not 2 <= words(anchor) <= 5:
        raise SystemExit(f"sentence anchor {anchor}")
    if text.count(anchor) != 1:
        raise SystemExit(f"anchor not once in sentence: {text}")
    linked = text.replace(
        anchor,
        f'<a href="{esc(href)}" {LINK}>{esc(anchor)}</a>',
        1,
    )
    return (
        '<p style="font-family:Manrope,sans-serif;font-size:0.95rem;line-height:1.6;color:#55555A;'
        f'margin:1.25rem auto;max-width:760px;padding:0 1.25rem;">{linked}</p>\n'
    )


def main() -> int:
    names = load_projects()
    pages = {}
    for path in verify.html_files():
        pages[path] = strip_inserted(path.read_text(encoding="utf-8", errors="replace"))

    home = ROOT / "index.html"
    pages[home] = restore_home_hero(pages[home])

    # Maps from hub cards.
    area_projects: dict[str, list[str]] = {}
    dev_projects: dict[str, list[str]] = {}
    project_area: dict[str, str] = {}
    project_dev: dict[str, str] = {}
    for slug in AREA_LABEL:
        if slug.endswith("-bengaluru"):
            continue
        path = ROOT / "property/area" / slug / "index.html"
        slugs = projects_on(pages[path])
        area_projects[slug] = slugs
        for project in slugs:
            project_area[project] = slug
    for slug in DEV_LABEL:
        path = ROOT / "property/developer" / slug / "index.html"
        slugs = projects_on(pages[path])
        dev_projects[slug] = slugs
        for project in slugs:
            project_dev[project] = slug

    def area_items(slug: str) -> list[tuple[str, str]]:
        zone = AREA_ZONE[slug]
        areas = ZONES[zone]
        index = areas.index(slug)
        items = []
        for step in range(1, len(areas)):
            other = areas[(index + step) % len(areas)]
            items.append((f"/property/area/{other}/", place_anchor(other)))
            if len(items) == 3:
                break
        items.append((f"/property/area/{zone}/", AREA_LABEL[zone]))
        items.append(("/property/", "All properties"))
        if len(items) < 3:
            items.append(("/calculators/", "Buyer calculators"))
        return items[:6]

    dev_slugs = sorted(DEV_LABEL)
    def dev_items(slug: str) -> list[tuple[str, str]]:
        index = dev_slugs.index(slug)
        items = []
        for step in range(1, 5):
            other = dev_slugs[(index + step) % len(dev_slugs)]
            items.append((f"/property/developer/{other}/", f"{DEV_LABEL[other]} projects"))
        items.append(("/property/", "All properties"))
        return items

    blocks: dict[Path, str] = {}

    # Project pages.
    for project, area in project_area.items():
        path = ROOT / "property" / project / "index.html"
        if path not in pages:
            continue
        siblings = [item for item in area_projects[area] if item != project][:3]
        items = [(f"/property/{item}/", names[item]) for item in siblings if item in names]
        items.append((f"/property/area/{area}/", f"{AREA_LABEL[area]} projects"))
        if project in project_dev:
            dev = project_dev[project]
            items.append((f"/property/developer/{dev}/", f"{DEV_LABEL[dev]} projects"))
        zone = AREA_ZONE[area]
        items.append((f"/property/area/{zone}/", AREA_LABEL[zone]))
        if len(items) < 3:
            items.append(("/property/", "All properties"))
            items.append(("/calculators/", "Buyer calculators"))
        blocks[path] = related_block("Nearby projects", items[:6])

    for path in pages:
        rel = str(path.relative_to(ROOT))
        if not rel.startswith("property/") or rel.count("/") != 2:
            continue
        if path in blocks or "/area/" in rel or "/developer/" in rel:
            continue
        blocks[path] = related_block(
            "Nearby projects",
            [
                ("/property/", "All properties"),
                ("/property/area/east-bengaluru/", "East Bengaluru"),
                ("/calculators/", "Buyer calculators"),
            ],
        )

    # Area, zone, developer hubs: plain intro, then a short block.
    for slug, label in AREA_LABEL.items():
        path = ROOT / "property/area" / slug / "index.html"
        page = pages[path]
        count = page.count('class="hub-card"')
        kind = "zone" if slug.endswith("-bengaluru") else "area"
        intro = hub_intro("zone" if kind == "zone" else "area", label, count)
        if 'class="hub-grid"' in page and 'class="hub-intro"' not in page:
            page = page.replace('<div class="hub-grid">', intro + '\n    <div class="hub-grid">', 1)
        pages[path] = page
        if kind == "zone":
            areas = ZONES[slug]
            items = [(f"/property/area/{item}/", place_anchor(item)) for item in areas]
            if len(items) < 3:
                items.append(("/property/", "All properties"))
                items.append(("/calculators/", "Buyer calculators"))
            blocks[path] = related_block("Nearby areas", items[:6])
        else:
            blocks[path] = related_block("Nearby areas", area_items(slug))

    for slug, label in DEV_LABEL.items():
        path = ROOT / "property/developer" / slug / "index.html"
        page = pages[path]
        count = page.count('class="hub-card"')
        intro = hub_intro("developer", label, count)
        if 'class="hub-grid"' in page and 'class="hub-intro"' not in page:
            page = page.replace('<div class="hub-grid">', intro + '\n    <div class="hub-grid">', 1)
        pages[path] = page
        blocks[path] = related_block("Other developers", dev_items(slug))

    # Property index, site pages, calculator hub.
    blocks[ROOT / "property/index.html"] = related_block(
        "Browse by zone",
        [
            ("/property/area/east-bengaluru/", "East Bengaluru"),
            ("/property/area/north-bengaluru/", "North Bengaluru"),
            ("/property/area/south-bengaluru/", "South Bengaluru"),
            ("/property/area/west-bengaluru/", "West Bengaluru"),
            ("/property-consultant-bengaluru/", "Property consultant"),
        ],
    )
    blocks[ROOT / "calculators/index.html"] = related_block(
        "Related reading",
        [
            ("/calculators/future-property-value-calculator/", "Future value calculator"),
            ("/calculators/hni-home-affordability-calculator/", "HNI affordability calculator"),
            ("/calculators/north-bangalore-investment-calculator/", "North Bengaluru calculator"),
            ("/calculators/parking-cost-calculator/", "Parking cost calculator"),
            ("/calculators/roi-comparison-calculator/", "ROI comparison"),
            ("/calculators/moving-cost-calculator/", "Moving cost calculator"),
        ],
    )
    blocks[ROOT / "contact/index.html"] = related_block(
        "Related reading",
        [
            ("/property-consultant-bengaluru/", "Property consultant"),
            ("/careers/", "Open roles"),
            ("/property/", "Reviewed properties"),
            ("/calculators/", "Buyer calculators"),
        ],
    )
    blocks[ROOT / "careers/index.html"] = related_block(
        "Related reading",
        [
            ("/contact/", "Talk to us"),
            ("/property-consultant-bengaluru/", "Property consultant"),
            ("/property/", "Reviewed properties"),
            ("/calculators/", "Buyer calculators"),
        ],
    )
    blocks[ROOT / "property-consultant-bengaluru/index.html"] = related_block(
        "Related reading",
        [
            ("/contact/", "Talk to us"),
            ("/property/", "Reviewed properties"),
            ("/calculators/", "Buyer calculators"),
            ("/careers/", "Open roles"),
        ],
    )
    role_paths = {
        "home-buyer-advisor": "Home buyer advisor",
        "property-consultant-inside-sales": "Inside sales role",
        "executive-assistant-to-the-founder": "Founder assistant role",
    }
    for slug, label in role_paths.items():
        path = ROOT / "careers" / slug / "index.html"
        others = [(f"/careers/{other}/", role_paths[other]) for other in role_paths if other != slug]
        items = others + [("/careers/", "Open roles"), ("/contact/", "Talk to us")]
        blocks[path] = related_block("Related reading", items)

    for path, block in blocks.items():
        if path not in pages:
            raise SystemExit(f"missing {path}")
        pages[path] = insert_before_footer(pages[path], block)

    for rel, (text, href, anchor) in CALC_SENTENCES.items():
        path = ROOT / rel
        page = pages[path]
        marker = '<section class="ak-more-calcs-section"'
        if marker not in page:
            raise SystemExit(f"no related section on {rel}")
        note = sentence_html(text, href, anchor)
        pages[path] = page.replace(marker, note + marker, 1)

    for path, text in pages.items():
        path.write_text(text, encoding="utf-8")

    # Planned-link report against in-text links.
    fresh = {path: path.read_text(encoding="utf-8", errors="replace") for path in verify.html_files()}
    present = defaultdict(set)
    for path, page in fresh.items():
        if not verify.is_content(path) and str(path.relative_to(ROOT)) != "index.html":
            pass
        base = verify.page_base(path)
        body = verify.main_slice(page)
        rel = str(path.relative_to(ROOT))
        source = "https://acrenkey.com/" if rel == "index.html" else "https://acrenkey.com/" + rel[: -len("index.html")]
        for href, _text, _pos in verify.extract_anchors(body):
            local = verify.local_target(href, base)
            if local:
                present[source.rstrip("/") + "/"].add(local)
            host = ""
            if href.startswith("http"):
                present[source.rstrip("/") + "/"].add(href.split("?")[0])

    with PLAN.open(newline="", encoding="utf-8") as handle:
        plan = list(csv.DictReader(handle))
    skipped = []
    placed = 0
    for row in plan:
        source = row["source"] if row["source"].endswith("/") else row["source"] + "/"
        target = row["target"]
        path = verify.file_for_source(row["source"])
        found = False
        if path and path.exists():
            page = fresh[path]
            base = verify.page_base(path)
            body = verify.main_slice(page)
            for href, _text, _pos in verify.extract_anchors(body):
                if verify.href_matches(href, target):
                    found = True
                    break
                local = verify.local_target(href, base)
                host, tpath = verify.norm_path(target)
                if local and local == tpath and host in ("", "acrenkey.com", "www.acrenkey.com"):
                    found = True
                    break
        if found:
            placed += 1
        else:
            skipped.append(row)
    out = ROOT / "scripts" / "skipped-links.csv"
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["source", "target", "anchor", "placement", "reason"])
        writer.writeheader()
        for row in skipped:
            writer.writerow(
                {
                    "source": row["source"],
                    "target": row["target"],
                    "anchor": row["anchor"],
                    "placement": row.get("placement", ""),
                    "reason": "No natural sentence on this page. The related block holds at most six contextual items.",
                }
            )
    print(f"placed {placed} skipped {len(skipped)} of {len(plan)}")
    hero = fresh[home]
    h = hero[hero.find("hero-kicker"): hero.find("framework-section")]
    plain = re.sub(r"<[^>]+>", " ", h)
    print("HERO", " ".join(html_lib.unescape(plain).split())[:400])
    print("explore left", fresh[home].count("Explore by area"), "related left", sum(t.count("ak-inline-related") for t in fresh.values()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
