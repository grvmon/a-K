---
name: acrenkey-style-guide
description: Authoritative acre&key Master Style Guide v2.1. Enforces the strict 6-token WCAG AAA color palette (zero other colors allowed), geometry (4px radius, 0.5px hairline borders, zero default shadows), brand lexicon (no independent/unbiased), compliance rules, channel voice, SEO/AEO writing, and formatting standards across all pages and content.
---

# acre&key Master Style Guide & Design System (v2.1)

Authoritative design, brand, and editorial standard for acre&key (`acrenkey.com`). All bots, writers, designers, and developers must follow these rules without exception.

---

## 1. The Strict 6-Token Master Color Palette (100% WCAG AAA Certified)

> [!CAUTION]
> **Zero Rogue Color Mandate**: NO color is permitted on any page or asset other than this exact 6-token system. All legacy brass (`#7D442A`, `#8C6734`), random beiges (`#FAF7F2`), SaaS blues, or arbitrary grays are strictly banned.

| Token | Hex / Value | CSS Variable | Functional Role & Contrast |
|---|---|---|---|
| **Titanium Frost Canvas Base** | `#FAFAFA` | `--titanium-frost` | 70% positive-space foundation canvas and frosted HUD surfaces. Eliminates pure white glare. |
| **Obsidian Black Ink** | `#2B2D31` | `--obsidian-black` | Primary editorial ink, display headings, dark breakout surfaces, anchored scrim overlays (13.22:1 AAA on Titanium Frost). |
| **Text Copper AAA** | `#804526` | `--text-copper-aaa` | Section kickers, inline links, key metrics, and colored text on light backgrounds (7.19:1 AAA on Titanium Frost). |
| **Primary CTA Copper Gradient** | `linear-gradient(135deg, #E88D67 0%, #9E3F23 100%)` | `--cta-gradient` | Primary conversion action buttons only. Pair with subtle optical text shadow `0 1px 2px rgba(43,45,49,0.35)` to protect white glyph contrast. |
| **Highlight Peach** | `#E88D67` | `--highlight-peach` | Used **ONLY on dark backgrounds** for badges, accents, and focus rings (7.92:1 AAA on anchored scrims). Never use for body text on light surfaces. |
| **Muted Slate Body Ink** | `#55555A` | `--neutral-grey` | Long-form analytical paragraphs, captions, secondary ledger labels (7.10:1 AAA on Titanium Frost). |

---

## 2. Layout, Geometry & Motion Physics

1. **Corner Radius (Strictly 4px)**:
   - `border-radius: 4px` across all cards, modals, buttons, inputs, tags, and badges.
   - **No Pills**: `border-radius: 999px` is strictly banned. Status tags and badges must be 4px rounded rectangles.
2. **Hairline Borders (0.5px)**:
   - Dividers and borders must be `0.5px solid rgba(85, 85, 90, 0.2)` to mimic high-end architectural print and financial sheets.
3. **Zero Default Shadows on Static Cards**:
   - No SaaS drop shadows on static data cards. Cards rely on 0.5px hairlines, whitespace (min `1.5rem` padding), and typographic contrast.
4. **Cinematic Transitions**:
   - Smooth `0.4s ease` (400ms) on all interactive transitions. Images dim slightly on hover (400ms fade), no physical lifting or popping.
5. **Text-on-Image Legibility (Anchored Gradient Rule)**:
   - Never place text directly over imagery. Apply an Obsidian Black anchored scrim:
     `linear-gradient(to top, rgba(10, 10, 11, 0.95) 0%, rgba(10, 10, 11, 0) 60%)`.

---

## 3. Typography

- **Headings & Display**: `'Cormorant Garamond', serif` (Weight 400 strictly. Never faux-bold).
- **Body & UI Elements**: `'Manrope', sans-serif` (Weights 400, 500, 600, 700).
- **Fluid Sizing**: Use `clamp()` for responsive headings without jumpy media query shifts.

---

## 4. Brand Name & Legal Identity (Section 27)

- **Brand Name**: `acre&key`, always lowercase, no spaces around the `&`. It stays lowercase even at the start of a sentence.
- **Never**: `Acre&Key`, `Acre & Key`, `ACRE&KEY`, `AcreNKey`, `Acre and Key`.
- **Domain & Handles**: `acrenkey.com`, `@acreNkey` (official social handles).
- **Legal Entity Name**: `Acrenkey Realty LLP`. Use in the footer, agreements, invoices, privacy policy, RERA disclosure, and schema `legalName`. Not in marketing headlines.
- **In Code & HTML**: Write `acre&amp;key` in HTML attributes and meta, and `acre&key` in JSON-LD.
- **Founder & Author**: Gaurav Mongia, "Founder & Principal Advisor, acre&key". LinkedIn: `https://www.linkedin.com/in/gaurav-a-mongia`.
- **Logo**: Use approved SVGs only. Never retype the logo in an ad-hoc font.

---

## 5. Trust & Compliance Rules (Section 28)

1. **No Project Prices**: Never publish specific project prices on public pages, social media, or ads. Direct users to an advisory call or private cost sheet.
2. **No Negative Naming**: Never speak disparagingly about builders or rival projects. Present verified facts from RERA or court records neutrally.
3. **No Advisory Comparisons**: Never compare acre&key with other advisory firms, brokers, or portals.
4. **No Unbacked Claims**: Banned: "69-point", "saves 3x", "cuts tenure in half", "guaranteed", "best", "No.1", unless backed by verified math shown on the page.
5. **Tax Content Disclaimer**: Mandatory note: *"Indicative only. Please verify with your Chartered Accountant before acting."*
6. **Legal Content Disclaimer**: Mandatory note: *"General information, not legal advice. Please consult a property lawyer."*
7. **Official Sources Only**: Every rate, stamp duty slab, or threshold must cite official authorities (IGR Karnataka/Kaveri, Karnataka Gazette, RBI, Income Tax Dept, GST Council, K-RERA, BBMP/GBA).
8. **RERA Disclosure**: The agent RERA registration number and legal entity name (`Acrenkey Realty LLP`) belong in the site footer. If developer commission is earned, disclose clearly as a sales partner.
9. **Privacy**: Never publish client names, unit numbers, or purchase documents without express written consent.
10. **Zero Artificial Urgency**: Never use "last few units", "price rising soon", or countdown timers.

---

## 6. Brand-Banned Words & AI Tells (Section 29)

### Brand-Banned Vocabulary
- **Strictly banned everywhere**: `independent`, `objective`, `unbiased`, `neutral advisor`, `100%`, `guaranteed`, `best`, `perfect`, `No.1`, `top-rated`, `luxury` (in hero/CTAs), `premium` (in hero/CTAs), `dream home`, `breathtaking`, `masterpiece`, `once-in-a-lifetime`, `hurry`, `don't miss`, `limited time`, `hassle-free`, `one-stop solution`.
- **Approved alternatives**:
  - `independent` -> `buyer-first`, `free` (for tools/calculators)
  - `objective` -> `evidence-based`, `structured`, `data-driven`
  - `unbiased shortlist` -> `curated shortlist`, `checked with structured due diligence`
  - `luxury/premium` -> `institutional-grade`, `A-grade` (display text)
  - `features/amenities` -> `asset fundamentals`, `township infrastructure`
  - `buy now / submit` -> `Request Advisory Call`, `Get Buyer Analysis`

### AI Tells (Purge on Every Human-Facing Draft)
- **Forbidden words**: `delve`, `navigate the landscape`, `in today's fast-paced world`, `tapestry`, `realm`, `embark`, `unlock`, `elevate`, `seamless`, `robust`, `leverage` (as verb), `pivotal`, `crucial`, `game-changer`, `holistic`, `empower`, `testament to`, `it's worth noting`, `in conclusion`, `ultimately`.
- **Forbidden patterns**: "It's not just X, it's Y"; triplets of adjectives; rhetorical opener questions; every paragraph ending in a neat moral summary; heavy em-dashes; emoji bullet lists; "Great question!".

---

## 7. Content Templates by Type (Section 30)

- **30.1 Answers Page (`answers.acrenkey.com`)**:
  Byline at top only ("By Gaurav Mongia, acre&key · Updated DD Mon YYYY"). H1 as question, 40-60 word direct answer snippet, H2s as sub-questions, Bengaluru example, 3-6 FAQs, sources, CA/lawyer disclaimer, 3-5 related answers. Schema: `QAPage` / `Article` + `FAQPage` + `BreadcrumbList` + `Person`.
- **30.2 Calculator Page (`acrenkey.com/calculators/...`)**:
  Follow the `calculator-page-seo-aeo` skill: Breadcrumb, H1, Last Updated, 40-60 word direct answer lead with formula & worked example, calculator tool with default inputs, How to Use, Formula & Method, Scenario Table, Bengaluru Notes, Assumptions, FAQs, Sources, Disclaimer, and soft CTA.
- **30.3 Blog Post (`acrenkey.com/blogs/`)**:
  H1 under 65 chars, direct-answer intro under 80 words, table or checklist, FAQs, sources, author byline, 1,200-2,000 words, 3+ internal links.
- **30.4 Area Guide (Bengaluru Micro-Markets)**:
  Hard facts only: connectivity (metro, ORR, STRR, airport time), social infrastructure, civic jurisdiction (BBMP/GBA/BDA), water & drainage from official sources, upcoming projects list from RERA (no prices, no builder rankings).

---

## 8. Voice by Channel (Section 31)

Core tone everywhere: calm, specific, buyer-first, plain Indian English, zero hype.

| Channel | Length | Tone | Link Policy | Notes |
|---|---|---|---|---|
| **Website / Answers** | As needed | Expert, analytical, helpful | Internal links | Direct answer in first 60 words |
| **Quora** | 150-400 words | First-person, practical | Link only if directly answering | Answer fully in-post; disclose acre&key affiliation |
| **Reddit** | 80-250 words | Peer-to-peer, modest | Avoid links unless asked | Strict subreddit compliance, zero self-promotion |
| **LinkedIn (Gaurav)** | 80-200 words | Founder insight, one idea | Link in comments if needed | Max 3 hashtags, zero engagement bait |
| **WhatsApp (Clients)** | 2-5 lines | Warm, clinical, clear | Send documents as PDF | Business hours only (10 AM - 7 PM IST) |
| **Email** | 80-200 words | Professional, concise | One clear CTA | Subject line < 60 chars; sign-off "Gaurav Mongia, acre&key" |

---

## 9. SEO & AEO Writing Standards (Section 32)

- **Title**: 50-60 characters, primary keyword first, ending in `| acre&key`.
- **Meta Description**: 140-160 characters, states what page delivers, contains primary keyword, 0 banned words.
- **H1**: Exactly one per page. H2s phrased as questions real buyers search.
- **Direct Answer**: First 40-60 words under H1 must answer the core question with key figures and sources.
- **FAQs**: 3-8 per page, 40-80 words each, matching schema `FAQPage` word-for-word.
- **Bylines**: Top of page only with author Gaurav Mongia linked.
- **Dates**: Visible "Updated DD Mon YYYY" matching schema `dateModified`.
- **No Near-Duplicate Pages**: Every page must have unique data, formula, and local examples.

---

## 10. Formatting Basics (Section 33)

- **Language**: Indian English spelling (colour, centre, programme, organise).
- **City Name**: "Bengaluru" in body copy. "Bangalore" allowed once per page for search intent.
- **Dates**: Format as `DD Mon YYYY` (e.g., `18 Oct 2026`). Never US `MM/DD/YYYY`.
- **Currency**: `₹` with space before number, using `Cr` and `L` with two decimals (`₹ 3.10 Cr`, `₹ 85.00 L`). Exact numbers use Indian grouping (`₹ 3,10,00,000`).
- **Area**: Format as `3,150 Sq.Ft.`. Carpet area is mandatory for RERA comparisons.
- **Percentages**: `6.5%` (no space), interest rates as `8.50% p.a.`.
- **Abbreviations**: Spell out on first use: Karnataka Real Estate Regulatory Authority (K-RERA), Occupancy Certificate (OC), Encumbrance Certificate (EC).

---

## 11. Style Guide Page (`/style-guide/`) Section Index (00–33)

00. Governance & Versioning
01. Brand Foundation
02. Verbal Identity & Lexicon
03. Color Palette (WCAG AAA)
04. Identity & Logo Architecture
05. Typography Hierarchy & Guidelines
06. Layout & Spacing
07. Responsive System
08. Motion & Geometry Physics
09. Graphic Language
10. Photographic Art Direction
11. Actions & Inputs
12. Data & Tools
13. Templates & Patterns
14. Property Pages
15. Data Visualization
16. Maps & Location
17. Social Media
18. Paid Advertising
19. Video Identity
20. Editorial System
21. PDF Reports
22. SEO Design System
23. Design Tokens
24. Accessibility & Contrast Standards
25. Trust & Compliance
26. Governance & Contribution
27. Brand Name & Legal Identity
28. Trust & Compliance Rules
29. Banned Words & AI Tells
30. Content Templates by Type
31. Voice by Channel
32. SEO & AEO Writing Rules
33. Formatting Basics
