# Acre & Key Design System — One-Page Quick Reference (v2.0.1)

> **Release:** Version 2.0.1 (Apple-Grade Architectural Release) · October 2026  
> **Compliance:** 100% WCAG AAA Certified  
> **Audience:** Human Designers, Frontend Engineers, and Autonomous AI Agents

---

## 1. Wordmark & Logo Standards
- **Wordmark:** Strictly lowercase `acre&key` set in `Josefin Sans` (Weight 400).
- **Proportions:** Ampersand (`&`) sits baseline-aligned without scaling tricks.
- **Clear Space:** Minimum $1\times$ the height of the "k" on all four sides.
- **Permitted Colorways:** 
  - Obsidian Black (`#2B2D31`) on light canvas.
  - Pure White (`#FFFFFF`) on dark surfaces.
- **Strict Bans:** No gradients on the logo, no uppercase letters, no icon mark separation, no drop shadows.

---

## 2. Master Color Tokens (6-Token WCAG AAA System)

| Token Name | CSS Custom Property | Hex / Value | Architectural Role | Contrast Ratio & Standard |
| :--- | :--- | :--- | :--- | :--- |
| **Obsidian Black** | `--obsidian-black` | `#2B2D31` | Primary headings, dark canvas, display text | **13.2:1** (WCAG AAA Pass) |
| **Titanium Frost** | `--titanium-frost` | `#FAFAFA` | Master canvas base, light card backgrounds | Canvas base |
| **Primary Copper** | `--cta-gradient` | `linear-gradient(135deg, #E88D67 0%, #9E3F23 100%)` | Interactive primary CTA buttons only | **6.58:1** (WCAG AA Pass) |
| **Text Copper AAA**| `--text-copper-aaa` | `#804526` | Colored editorial text, active links on light | **7.19:1** (WCAG AAA Pass) |
| **Highlight Peach** | `--highlight-peach` | `#E88D67` | Accents & focus rings on Obsidian dark ONLY | **5.54:1** (Dark Canvas Pass) |
| **Muted Slate** | `--neutral-grey` | `#55555A` | Long-form body paragraphs, metadata, labels | **7.10:1** (WCAG AAA Pass) |

---

## 3. Typography Hierarchy & Rules
- **Display & Headings:** `Cormorant Garamond`, serif. Strictly Weight 400. Faux-bolding is banned.
- **Body & UI Elements:** `Manrope`, sans-serif (Weights 400 Regular, 500 Medium, 600 Semi-Bold, 700 Bold).
- **Heading Case:** Strictly **Sentence case** across all hero headlines, section H2s, and subheadings.
- **Exclamation Marks:** 100% Banned. Tone is clinical, objective, and institutional.
- **Currency Format:** Always `₹` with a space before amounts (e.g., `₹ 3.10 Cr`, `₹ 85 L`).
- **Area & Measurement Format:** Title Case with periods and commas for $>999$ (e.g., `3,150 Sq.Ft.`).

---

## 4. Layout, Geometry & Spacing
- **Corner Radius:** Strictly **`4px`** (`border-radius: 4px`) across all cards, buttons, badges, modals, and inputs.
  - *Anti-Pill Rule:* Never use `border-radius: 999px`.
- **Borders & Dividers:** Strictly **`0.5px` hairline borders** (`rgba(85, 85, 90, 0.2)`).
- **Container Max-Width:** Maximum `1280px` with `2rem` side padding.
- **Fibonacci Spacing Scale:**
  - `--space-xs`: `4px` (icon gaps)
  - `--space-sm`: `8px` (badge & internal item spacing)
  - `--space-md`: `16px` (card padding)
  - `--space-lg`: `24px` (sub-section gaps)
  - `--space-xl`: `40px` (section padding)
  - `--space-2xl`: `64px` (section margins)
  - `--space-3xl`: `104px` (hero vertical breathing room)
- **Zero Default Drop Shadows:** Do not use CSS drop shadows on data cards. Hierarchy is built using whitespace and 0.5px hairlines.
- **Functional Iconography (Strict 2px Stroke):**
  - Exclusively un-filled line icons with a strict `2px` stroke in Obsidian Black (`#2B2D31`) or Slate (`#55555A`).
  - Permitted only when they add analytical clarity (Diligence Checks, Statutory Fees & Costs, Asset Dimensions, Possession Timeline, RERA Verification, Corridor Nodes). Decorative or filled icons are strictly prohibited.

---

## 5. Photographic Art Direction & Image Treatments
- **Cinematic Desaturation Filter:** Apply `filter: saturate(0.85) contrast(1.05);` across all builder 3D architectural renders.
- **Anchored Gradient Rule:** Never place raw text directly over photography. Always anchor using the Obsidian Black gradient overlay:
  ```css
  background: linear-gradient(to top, rgba(10, 10, 11, 0.95) 0%, rgba(10, 10, 11, 0) 60%);
  ```
  *(Achieves 19.8:1 AAA contrast on white text).*
- **Aspect Ratios:** Property hero: `16:9` · Persona cards: `3:4` · Floorplans: `4:3`.
- **Motion & Hover:** Elements never physically lift. Images subtly zoom (`scale(1.03)`) or dim over `0.4s ease`.

---

## 6. Primary CTA & Clinical Lexicon Map

### Primary Button Styling
- Background: `var(--cta-gradient)` (`#E88D67 → #9E3F23`)
- Border-radius: `4px`
- Color: `#FFFFFF`
- Padding: `1rem 2rem`
- Hover: `opacity: 0.9` (400ms ease)

### Scoped Lexicon Translation

| Banned Consumer Fluff (Display / H1 / CTA) | Approved Clinical Advisory Term |
| :--- | :--- |
| "Buy Now" / "Submit" | **"Request Advisory Call"** / **"Get Buyer Analysis"** |
| "Luxury" / "Ultra-Luxury" / "Premium" | **"Institutional-Grade"** / **"A-Grade"** |
| "Amenities" / "Features" | **"Asset Fundamentals"** / **"Township Infrastructure"** |
| "Price List" | **"Valuation Matrix"** / **"Cost Sheet"** |
| "Brochure" | **"Asset Dossier"** / **"Project Brief"** |
| "Best" / "Dream Home" / "Exclusive" | **"Objective Evaluation"** / **"Verified Asset"** |

---

## 7. Social & Display Ad Dimensions

| Platform / Format | Dimensions | Aspect Ratio | Safe Margin Requirements |
| :--- | :--- | :--- | :--- |
| **Meta Feed / LinkedIn Post** | `1080 × 1080 px` | 1:1 | 64px padding all around |
| **Meta Story / Reels / Vertical** | `1080 × 1920 px` | 9:16 | 250px top/bottom system safe zones |
| **Display Ad / Landscape Link** | `1200 × 628 px` | 1.91:1 | Centered text over anchored gradient |
| **LinkedIn Company Cover** | `1584 × 396 px` | 4:1 | 300px left margin for profile avatar |
| **Print Dossier Report** | `210 × 297 mm` (A4) | 1:1.414 | 20mm margins, 10mm gutter |

---

## 8. AI Agent Code Generation Rules
1. **Never hardcode hex colors** in HTML/components — always reference CSS variables (`var(--titanium-frost)`, `var(--obsidian-black)`, etc.).
2. **Never generate pill badges** (`border-radius: 999px`). All badges must use `border-radius: 4px`.
3. **Never generate box-shadows** on standard cards (`box-shadow: none !important`).
4. **Never create bespoke site headers or footers**; reuse the unified platform navigation architecture.
5. **Always verify DPDP non-prechecked consent** on lead forms.
