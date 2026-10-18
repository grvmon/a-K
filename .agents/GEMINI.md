# acre&key Master Brand & Design Guidelines (100% WCAG AAA Certified, v2.1)

## 0. Brand Identity & Zero Rogue Color Mandate
- **Brand Name**: `acre&key` (always lowercase, no spaces around the `&`). Never write `Acre&Key` or `Acre & Key`.
- **Legal Entity**: `Acrenkey Realty LLP` (used in footer, legal disclosures, schema `legalName`).
- **Zero Rogue Color Mandate**: NO color is permitted on any page or asset other than the certified 6-token master palette below. All legacy brass (`#7D442A`, `#8C6734`), random beiges (`#FAF7F2`), SaaS blues, or arbitrary grays are strictly banned.

## 1. Master Color Palette (Strict WCAG AAA Certified)
- **Primary CTA Copper Gradient (`--cta-gradient`)**: `linear-gradient(135deg, #E88D67 0%, #9E3F23 100%)` (Pair with text shadow `0 1px 2px rgba(43,45,49,0.35)` to protect white glyph contrast).
- **Text Copper AAA (`--text-copper-aaa`)**: `#804526` (Must be used for all colored text, section kickers, pillar numerals, and links on light backgrounds to pass 7.0:1 contrast).
- **Highlight Peach (`--highlight-peach`)**: `#E88D67` (Used **ONLY on dark backgrounds** for badges, accents, and focus rings).
- **Titanium Frost Canvas Base (`--titanium-frost`)**: `#FAFAFA` (Foundation canvas, eliminates harsh white glare).
- **Obsidian Black (`--obsidian-black`)**: `#2B2D31` (Display headings, dark breakout surfaces, primary editorial ink; 13.22:1 AAA).
- **Muted Slate (`--neutral-grey`)**: `#55555A` (Body paragraphs, captions, secondary ledger labels; 7.10:1 AAA).

## 2. Typography
- **Headings & Display**: `'Cormorant Garamond', serif` (Must always be weight 400. Do not faux-bold).
- **Body & UI Elements**: `'Manrope', sans-serif` (Weights 400, 500, 600, 700).
- **Fluid Scale**: Headings must use `clamp()` functions to scale fluidly without media queries.
- **Icons**: Line icons • 2px stroke • Obsidian Black. Use only when they add clarity.

## 3. Layout & Geometry (HNI Architectural Precision)
- **Container Widths**: Maximum container width is **1280px** with `2rem` side padding.
- **Corner Radius**: Strictly **`4px`** (`border-radius: 4px`) across all cards, modals, buttons, and badges. (No soft 8px, no brutalist 0px).
- **Borders & Dividers**: Strictly **`0.5px` hairline borders** (`rgba(85, 85, 90, 0.2)`) to mimic high-end financial spreadsheets and editorial print.

## 4. Interaction & Motion Design
- **Hover States (Cinematic & Flat)**: Elements do NOT physically lift (no heavy drop shadows). Interactions are cinematic: images slightly dim with a smooth 400ms fade.
- **Transition Timing**: All transitions operate on a deliberate, luxurious `0.4s ease` (400ms).

## 5. Photographic Art Direction
- **Cinematic Desaturation**: All builder-provided 3D renders must be filtered via CSS (`filter: saturate(0.85) contrast(1.05);`) to ensure a moody, cohesive, high-end editorial grade across the platform.

## 6. Lexicon & Tone of Voice
- **Brand-Banned Vocabulary**: Never use `independent`, `objective`, `unbiased`, `neutral advisor`, `100%`, `guaranteed`, `best`, `perfect`, `No.1`, `69-point`, `top-rated`, `luxury` (in hero/CTAs), `premium` (in hero/CTAs), `dream home`, `breathtaking`, `masterpiece`, `once-in-a-lifetime`, `hurry`, `don't miss`, `limited time`, `hassle-free`, `one-stop solution`.
- **Approved Lexicon Replacements**:
  - `independent` -> `buyer-first`, `free` (for calculators/tools)
  - `objective` -> `evidence-based`, `structured`, `data-driven`
  - `Buy Now` -> `Request Advisory Call`
  - `Submit` -> `Get Buyer Analysis`
  - `Luxury/Premium` -> `Institutional-Grade`, `A-Grade` (in display text)
  - `Features/Amenities` -> `Asset Fundamentals`, `Township Infrastructure` (in display text)
  - `Price List` -> `Valuation Matrix`, `Cost Sheet` (never publish project prices publicly)
  - `Brochure` -> `Asset Dossier`, `Project Brief`

## 7. Global Header & Footer Standard Rule
- **Standard Sitewide Footer Mission**:
  > *"Buyer-first home buying advisory in Bengaluru. We help home buyers, HNI investors and corporate leaders shortlist and check properties with structured due diligence."*
- **Header & Footer Consistency**: For all new and existing pages, ALWAYS use the exact standard site header and site footer matching the main architecture. Do NOT create custom or simplified variants. Include RERA registration number and legal name (`Acrenkey Realty LLP`).

## 8. Forms & Inputs (Zero Bubbly UIs)
- **Geometry**: Inputs and Select dropdowns must have strictly `4px` radiuses.
- **Borders**: Strictly `0.5px` borders (`rgba(85, 85, 90, 0.2)`).
- **Focus States**: Bottom-border or full-border color shifts to Text Copper (`#804526`) with a 0.4s transition.

## 9. Badges & Tags (The Anti-Pill Rule)
- **No Pills**: Do NOT use `border-radius: 999px` (pill-shaped tags).
- **Rectangular Authority**: All status tags, RERA badges, and scoring badges must be `4px` rounded rectangles with a subtle 0.5px border.

## 10. Cinematic Modals & Overlays
- **Backdrops**: Modals must blur the background natively using `backdrop-filter: blur(8px)`.
- **Overlay Color**: Use `rgba(10,10,10,0.85)` for a deep, desaturated cinematic dimming effect instead of flat black.

## 11. Text-on-Image Legibility (The Anchored Gradient Rule)
- **No Raw Text**: Never place text directly over an image without protection.
- **Gradient Anchors**: Always apply an Obsidian Black linear gradient overlay (`linear-gradient(to top, rgba(10, 10, 11,0.95) 0%, rgba(10, 10, 11,0) 60%)`) anchoring the text from the bottom (or top) to guarantee 7.0:1 AAA contrast.

## 12. Editorial Cards (Zero Default Shadows)
- **No Floating Cards**: Do NOT use default CSS drop shadows on static data cards.
- **Architectural Hierarchy**: Cards must rely on `0.5px` hairlines, pure whitespace (min `1.5rem` padding), and strict typography scales to create structure.

## 13. Inline Link Behavior
- **No Default Blue**: Never use default browser blue links.
- **Luxury Underlines**: Inline links must use `--text-copper-aaa` (`#804526`) with a `1px` thick underline offset by `text-underline-offset: 4px;` or `6px;`.
- **Hover State**: The underline should be slightly transparent (`rgba(128,69,38,0.3)`) and turn fully solid on hover over `0.4s`.

## 14. Compliance & Disclaimers
- **Tax Content**: *"Indicative only. Please verify with your Chartered Accountant before acting."*
- **Legal Content**: *"General information, not legal advice. Please consult a property lawyer."*
- **Official Sources**: Every rate, fee, slab, or legal threshold must cite official authorities (IGR Karnataka/Kaveri, Karnataka Gazette, RBI, Income Tax Dept, GST Council, K-RERA, BBMP/GBA).
