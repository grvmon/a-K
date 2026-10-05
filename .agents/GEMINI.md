# Acre & Key Brand & Design Guidelines (100% WCAG AAA Certified)

## 1. Master Color Palette (Strict WCAG AAA Certified)
- **Primary CTA Copper Gradient (`--cta-gradient`)**: `linear-gradient(135deg, #E88D67 0%, #9E3F23 100%)`
- **Text Copper AAA (`--text-copper-aaa`)**: `#804526` (Must be used for all colored text on light backgrounds to pass 7.0:1 contrast).
- **Highlight Peach (`--highlight-peach`)**: `#e5b899` (Used only on dark backgrounds).
- **Titanium Frost Canvas Base (`--titanium-frost`)**: `#FAFAFA`
- **Obsidian Black (`--obsidian-black`)**: `#1C1C1E`
- **Muted Slate (`--neutral-grey`)**: `#55555A` (Body paragraphs)

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
- **Scoped Lexicon Ban:** Standard industry terms like "Amenities", "Features", "Luxury", and "Premium" are **BANNED** in hero headlines, primary CTAs, and large display text (to maintain editorial authority). However, they are **ALLOWED** in metadata, alt-tags, and keyword-led H2s (e.g., "Township Amenities") to ensure SEO is not compromised.
- **Tone Do/Don't:** 
  - *Don't (Salesy):* "Buy now to get the best luxury features!"
  - *Do (Clinical/Advisory):* "Analyze the asset fundamentals and micro-market infrastructure."
- **Expanded Lexicon Map:**
  - "Buy Now" -> "Request Advisory Call"
  - "Submit" -> "Get Buyer Analysis"
  - "Luxury/Premium" -> "Institutional-Grade", "A-Grade" (in display text)
  - "Features/Amenities" -> "Asset Fundamentals", "Township Infrastructure" (in display text)
  - "Price List" -> "Valuation Matrix", "Cost Sheet"
  - "Brochure" -> "Asset Dossier", "Project Brief"

## 7. Global Header & Footer Standard Rule
- **Header & Footer Consistency**: For all new and existing pages, ALWAYS use the exact standard site header and site footer matching the main architecture. Do NOT create custom or simplified variants.

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
- **Gradient Anchors**: Always apply a deep navy linear gradient overlay (`linear-gradient(to top, rgba(10, 10, 11,0.95) 0%, rgba(10, 10, 11,0) 60%)`) anchoring the text from the bottom (or top) to guarantee 7.0:1 AAA contrast.

## 12. Editorial Cards (Zero Default Shadows)
- **No Floating Cards**: Do NOT use default CSS drop shadows on static data cards. It looks like a cheap SaaS dashboard.
- **Architectural Hierarchy**: Cards must rely on `0.5px` hairlines, pure whitespace (min `1.5rem` padding), and strict typography scales to create structure.

## 13. Inline Link Behavior
- **No Default Blue**: Never use default browser blue links.
- **Luxury Underlines**: Inline links must use `--text-copper-aaa` with a `1px` thick underline that is offset by `text-underline-offset: 4px;` or `6px;`. 
- **Hover State**: The underline should be slightly transparent (`rgba(128,69,38,0.3)`) and turn fully solid on hover over `0.4s`.


## 14. Typography Updates
- **Headings**: `Marcellus`, serif (Must always be weight 400. Do not faux-bold).
- **Body**: `Manrope`, sans-serif.
- **Icons**: Line icons • 2px stroke • Navy. Use only when they add clarity.

## 15. Layout & Fibonacci Structure
- **Fibonacci Sequence**: Utilize the golden ratio sequence (1, 1, 2, 3, 5, 8...) for natural, aesthetically pleasing proportions in layout sizing, padding, and margins.
- **Rule of Thirds**: Use a grid system that brings focus to content by aligning key elements to the intersections of a 3x3 grid.

## 16. Visual Design (Shadows & Silhouettes)
- **70/30 Rule**: Use shadows and silhouettes to create depth. Maintain 70% light/positive space and 30% shadow/silhouette.
- **Perspective & Orthogonal Assets**: Digital and print assets must be rendered in 3D space to convey a premium, tangible quality.
