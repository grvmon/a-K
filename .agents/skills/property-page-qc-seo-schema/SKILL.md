---
name: property-page-qc-seo-schema
description: Audit, fix, and elevate any acre&key property dossier page (acrenkey.com/property/<slug>/) so it ranks #1 on Google, triggers commercial rich snippets (stars and price range), dominates Google AI Overviews, and meets 100% WCAG AAA brand compliance.
---

# acre&key Property Page QC, SEO & Schema Standard

Authoritative standard for every property page on acre&key (`acrenkey.com/property/<slug>/`).
Every property page is an institutional-grade, buyer-first due diligence dossier.
Follow this standard sequentially. Every section is **PASS** or **FIX**. A page ships only when all P0 items pass.

---

## 0. Brand & Compliance Rules (P0)

- [ ] **Brand Name Casing**: Strictly lowercase `acre&key` everywhere (meta, OG, Twitter, schemas, HTML headings, body copy, and social share scripts). Never `Acre&Key` or `Acre & Key`.
- [ ] **Legal Entity**: `Acrenkey Realty LLP` cited in footer, legal disclosures, and schema `legalName`.
- [ ] **Zero Rogue Color Mandate**: All legacy brass (`#7D442A`, `#8C6734`), random beiges (`#FAF7F2`), SaaS blues, or arbitrary grays are strictly banned.
  - **Text Copper AAA (`#804526`)**: Used for all colored text, section kickers, links, and icons on light backgrounds.
  - **Titanium Frost (`#FAFAFA`)**: Base section canvas.
  - **Obsidian Black (`#2B2D31`)**: Display headings, dark breakout surfaces, primary editorial ink.
  - **Muted Slate (`#55555A`)**: Body text, captions, secondary labels.
  - **CTA Copper Gradient**: `linear-gradient(135deg, #E88D67 0%, #9E3F23 100%)` with text shadow `0 1px 2px rgba(43,45,49,0.35)`.
- [ ] **Geometry**: Strictly `4px` corner radius (`border-radius: 4px;`) across all cards, modals, buttons, and badges. Hairline borders must be strictly `0.5px` (`rgba(85, 85, 90, 0.2)` or `rgba(10, 10, 11, 0.08)`).
- [ ] **Lexicon Replacements**:
  - `independent` -> `buyer-first`, `structured`, `data-driven`
  - `objective` / `unbiased` -> `evidence-based`, `structured`
  - `69-point` -> `structured due diligence` or `diligence memo`
  - `Luxury` / `Premium` (in hero/titles) -> `A-Grade`, `Institutional-Grade`, or remove
  - `Brochure` -> `Asset Dossier`, `Project Brief`

---

## 1. Canonical Breadcrumbs & Internal Linking (P0)

- [ ] **3-Tier Canonical Trail**:
  1. `Home` (`https://acrenkey.com/` or `/`)
  2. `Property in Bengaluru` (`https://acrenkey.com/property/` or `/property/`)
  3. `<Project Name>` (unlinked current page)
- [ ] **No 404 Intermediary Links**: Never include non-existent sub-directories (e.g. `/bengaluru/`, `/bengaluru/east-bengaluru/`).
- [ ] **Hover Styling**: `.page-breadcrumb a:hover { color: #804526 !important; }`.
- [ ] **Schema BreadcrumbList**: Exactly 3 items matching on-page DOM.

---

## 2. Page Speed & Core Web Vitals (P0)

- [ ] **Preload Hero Image**: In `<head>`, preload the LCP hero WebP asset:
  ```html
  <link rel="preload" as="image" href="../../style-guide/assets/<slug>/<hero-img>.webp?v=..." type="image/webp" fetchpriority="high">
  ```
- [ ] **Hero Image Attributes**:
  - `id="akMainHeroImage"` must have `fetchpriority="high"`, `decoding="async"`, and explicit intrinsic `width="800"` and `height="533"`.
  - Do NOT set `loading="lazy"` on the above-the-fold hero image.
- [ ] **Zero Unused Fonts**: Remove unused Google Font requests (e.g. `Josefin Sans`). Load only platform fonts (`Cormorant Garamond` and `Manrope`).
- [ ] **CLS Protection**: Every layout-affecting `<img>` (thumbnails, location cards, competitor cards) must have explicit `width` and `height` attributes with `loading="lazy"` and `decoding="async"`.
- [ ] **Fast TTFB**: Page transfer size gzipped under 100 KB; TTFB under 250ms on Cloudflare edge.

---

## 3. Image SEO & Art Direction (P0)

- [ ] **Format**: 100% `.webp` (or `.svg` for icons). No uncompressed `.jpg` or `.png`.
- [ ] **Naming Convention**: Project-scoped snake_case (e.g. `<project>_hero_<feature>_<angle>.webp`) and architectural kebab-case for floor plans (`unit-type-<slug>.webp`).
- [ ] **Contextual Keyword Alt Text**: Every single image must have a descriptive, non-generic alt tag specifying `<Project Name>`, feature, and location (e.g., `Prestige Evergreen Evening Swimming Pool and Tower Elevation View at Varthur Bangalore`).
- [ ] **Zero Text Overlays**: Pure photography and renders only; no baked-in text or marketing banners.
- [ ] **Photographic Grade**: Builder 3D renders must carry CSS desaturation filter: `filter: saturate(0.85) contrast(1.05);`.

---

## 4. Institutional Connected Knowledge Graph Schema (`@graph`) (P0)

Every property page must have a single unified `<script type="application/ld+json">` placed inside `<head>` with an interconnected `@graph` containing:

1. **`Product` & `ApartmentComplex`**:
   - `@id`: `https://acrenkey.com/property/<slug>/#project`
   - `name`: `<Project Name>`
   - `alternateName`: Array of 2–3 common search variations.
   - `image`: URL to high-res hero WebP.
   - `address`: `PostalAddress` with street, locality (`Bengaluru`), postalCode, and country (`IN`).
   - `geo`: `GeoCoordinates` with exact latitude and longitude.
   - `identifier`: `PropertyValue` citing official Karnataka RERA Project Registration ID (`PRM/KA/RERA/...`).
   - `offers`: `AggregateOffer` with `lowPrice`, `highPrice`, `priceCurrency: "INR"`, `offerCount`.
   - `aggregateRating`: `AggregateRating` with `ratingValue`, `bestRating: "5"`, `worstRating: "1"`, `ratingCount`.
   - `brand`: `Brand` with developer name.
2. **`BreadcrumbList`**:
   - `@id`: `https://acrenkey.com/property/<slug>/#breadcrumb`
   - 3 canonical levels (`Home` › `Property in Bengaluru` › `<Project Name>`).
3. **`FAQPage`**:
   - `@id`: `https://acrenkey.com/property/<slug>/#faq`
   - 4+ high-intent due diligence Q&As (RERA registration, on-road cost sheet, phases/delivery, traffic/water watchpoints).
4. **`Article`**:
   - `@id`: `https://acrenkey.com/property/<slug>/#article`
   - `about`: `{"@id": "https://acrenkey.com/property/<slug>/#project"}`
   - `publisher`: `{"@id": "https://acrenkey.com/#organization"}`
   - `author`: `Person` (`Gaurav Mongia`) with `url: "https://acrenkey.com/about-us"`
   - `mainEntityOfPage`: Canonical URL.
   - `datePublished` / `dateModified`: ISO 8601 with Indian Standard Time (`+05:30`).
5. **`RealEstateAgent` / `Organization`**:
   - `@id`: `https://acrenkey.com/#organization`
   - `name`: `acre&key`, `legalName`: `Acrenkey Realty LLP`
   - `identifier`: Karnataka RERA Agent Registration `PRM/KA/RERA/1251/446/AG/260814/007659`
   - `address`: Summit A, Brigade Metropolis, Mahadevapura, Bengaluru 560048
   - `hasMap`: Google Maps CID link.
   - `sameAs`: Official verified social profiles.
6. **`Review`**:
   - `@id`: `https://acrenkey.com/property/<slug>/#review`
   - `itemReviewed`: `{"@id": "https://acrenkey.com/property/<slug>/#project"}`
   - `publisher`: `{"@id": "https://acrenkey.com/#organization"}`
   - `author`: `Person` (`Gaurav Mongia`)
   - `reviewRating`: `Rating` with `ratingValue` matching project score.

---

## 5. Mobile & Desktop Responsiveness (P0)

- [ ] All data tables wrapped in `<div style="overflow-x:auto; -webkit-overflow-scrolling:touch; ...">`.
- [ ] No fixed pixel widths exceeding 100vw.
- [ ] Touch targets at least 44px x 44px on mobile devices.
- [ ] Modals styled with `max-height: calc(100vh - 2rem); overflow-y: auto;` and backdrop blur `backdrop-filter: blur(8px);`.
