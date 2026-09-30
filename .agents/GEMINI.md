# Acre & Key Brand & Design Guidelines (100% WCAG AAA Certified)
Reference: https://aabhisrv.github.io/ackey/style-guide/

## 1. Master Color Palette (Strict WCAG AAA Certified)
- **Primary CTA Copper Gradient (`--cta-gradient`)**: `linear-gradient(135deg, #be7555 0%, #9f5334 100%)`
- **Text Copper AAA (`--text-copper-aaa`)**: `#804526` (Must be used for all colored text on light backgrounds to pass 7.0:1 contrast).
- **Highlight Peach (`--highlight-peach`)**: `#e5b899` (Used only on dark backgrounds).
- **Warm Ivory Canvas Base (`--warm-ivory`)**: `#FAFAFA`
- **Deep Midnight Navy (`--deep-navy`)**: `#0A0A0B` / `#0A0A0B`
- **Muted Slate (`--muted-slate`)**: `#6E6E73` (Body paragraphs)

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

## 8. Forms & Inputs (Zero Bubbly UIs)
- **Geometry**: Inputs and Select dropdowns must have strictly `4px` radiuses.
- **Borders**: Strictly `0.5px` borders (`rgba(110, 110, 115, 0.2)`).
- **Focus States**: Bottom-border or full-border color shifts to Text Copper (`#804526`) with a 0.4s transition.

## 9. Badges & Tags (The Anti-Pill Rule)
- **No Pills**: Do NOT use `border-radius: 999px` (pill-shaped tags).
- **Rectangular Authority**: All status tags, RERA badges, and scoring badges must be `4px` rounded rectangles with a subtle 0.5px border.

## 10. Cinematic Modals & Overlays
- **Backdrops**: Modals must blur the background natively using `backdrop-filter: blur(8px)`.
- **Overlay Color**: Use `rgba(10,10,10,0.85)` for a deep, desaturated cinematic dimming effect instead of flat black.

## 11. Text-on-Image Legibility (The Anchored Gradient Rule)
- **No Raw Text**: Never place text directly over an image without protection.
- **Gradient Anchors**: Always apply a deep navy linear gradient overlay (`linear-gradient(to top, rgba(10, 10, 11,0.95) 0%, rgba(10, 10, 11,0) 60%)`) anchoring the text from the bottom (or top) to guarantee 7.0:1 AAA contrast.

## 12. Editorial Cards (Zero Default Shadows)
- **No Floating Cards**: Do NOT use default CSS drop shadows on static data cards. It looks like a cheap SaaS dashboard.
- **Architectural Hierarchy**: Cards must rely on `0.5px` hairlines, pure whitespace (min `1.5rem` padding), and strict typography scales to create structure.

## 13. Inline Link Behavior
- **No Default Blue**: Never use default browser blue links.
- **Luxury Underlines**: Inline links must use `--text-copper-aaa` with a `1px` thick underline that is offset by `text-underline-offset: 4px;` or `6px;`. 
- **Hover State**: The underline should be slightly transparent (`rgba(128,69,38,0.3)`) and turn fully solid on hover over `0.4s`.
