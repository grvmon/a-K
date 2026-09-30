# Acre & Key Brand & Design Guidelines (100% WCAG AAA Certified)
Reference: https://aabhisrv.github.io/ackey/style-guide/

## 1. Master Color Palette (Strict WCAG AAA Certified)
- **Primary CTA Copper Gradient (`--cta-gradient`)**: `linear-gradient(135deg, #be7555 0%, #9f5334 100%)`
- **Text Copper AAA (`--text-copper-aaa`)**: `#804526` (Must be used for all colored text on light backgrounds to pass 7.0:1 contrast).
- **Highlight Peach (`--highlight-peach`)**: `#e5b899` (Used only on dark backgrounds).
- **Warm Ivory Canvas Base (`--warm-ivory`)**: `#FBF6F3`
- **Deep Midnight Navy (`--deep-navy`)**: `#182A3D` / `#141D24`
- **Muted Slate (`--muted-slate`)**: `#33414C` (Body paragraphs)

## 2. Typography
- **Headings & Display**: `'Cormorant Garamond', serif` (Weight 400/500/700, editorial architectural luxury)
- **Body & UI Elements**: `'Manrope', sans-serif` (Weights 400, 500, 600, 700)
- **Fluid Scale**: Headings must use `clamp()` functions to scale fluidly without media queries.

## 3. Layout & Geometry (HNI Architectural Precision)
- **Container Widths**: Maximum container width is **1280px** with `2rem` side padding.
- **Corner Radius**: Strictly **`4px`** (`border-radius: 4px`) across all cards, modals, buttons, and badges. (No soft 8px, no brutalist 0px).
- **Borders & Dividers**: Strictly **`0.5px` hairline borders** to mimic high-end financial spreadsheets and editorial print.

## 4. Interaction & Motion Design
- **Hover States (Cinematic & Flat)**: Elements do NOT physically lift (no heavy drop shadows). Interactions are cinematic: images slightly dim with a smooth 400ms fade.
- **Transition Timing**: All transitions operate on a deliberate, luxurious `0.4s ease` (400ms).

## 5. Photographic Art Direction
- **Cinematic Desaturation**: All builder-provided 3D renders must be filtered via CSS (`filter: saturate(0.85) contrast(1.05);`) to ensure a moody, cohesive, high-end editorial grade across the platform.

## 6. Lexicon & Tone of Voice
- **BANNED**: "Buy Now", "Submit" -> **USE**: "Request Advisory Call", "Get Buyer Analysis"
- **BANNED**: "Luxury", "Premium" -> **USE**: "Institutional-Grade", "A-Grade"
- **BANNED**: "Features", "Amenities" -> **USE**: "Asset Fundamentals", "Township Infrastructure"

## 7. Global Header & Footer Standard Rule
- **Header & Footer Consistency**: For all new and existing pages, ALWAYS use the exact standard site header and site footer matching the main architecture. Do NOT create custom or simplified variants.
