# Acre & Key Brand & Design Guidelines (100% WCAG AAA Certified)
Reference: https://aabhisrv.github.io/ackey/style-guide/

## 1. Master Color Palette (Strict WCAG AAA Certified)
- **Primary CTA Button Gold (`--refined-brass` / `--antique-brass`)**: `#8C6734`
  - Contrast with `#FFFFFF` white text: **5.12 : 1** (exceeds WCAG AAA requirement of 4.5:1 for large/bold UI).
  - Used for: Primary CTA buttons (`.sd-btn-gold`, `.nav-cta-btn`, `.mobile-drawer-cta`).
- **Editorial Heading Highlight Gold (`--highlight-gold`)**: `#684A20`
  - Contrast on Warm Ivory (`#FBF6F3`): **7.56 : 1** (exceeds strict WCAG AAA requirement of 7.0:1).
  - Used for: Italic heading emphasis keywords (`.highlight-brass`, `.framework-title-gold`).
- **Step Numerals & Badges (`--step-brass` / `--dark-brass`)**: `#5E4119`
  - Contrast on Warm Ivory (`#FBF6F3`): **8.72 : 1** (exceeds strict WCAG AAA requirement of 7.0:1).
  - Used for: Step numbers (01–04), kicker category indicators, and framework badges.
- **Warm Ivory Canvas Base (`--warm-ivory`)**: `#FBF6F3`
  - Used for: 75% site background canvas with subtle ambient gold radial lighting glows and `soft-light` paper noise texture.
- **Deep Midnight Navy (`--deep-navy` / `--deep-navy-100`)**: `rgba(24, 42, 61, 0.84)` / `#182A3D`
  - Contrast on Warm Ivory (`#FBF6F3`): **13.62 : 1** (WCAG AAA).
  - Used for: All primary titles, H1–H4 headings, 1-line Summary Banner boxes, mobile drawer headers, and site footer foundation.
- **Body & Paragraph Text (`--deep-slate` / `--charcoal-ink`)**: `#303F4F` / `#374151`
  - Contrast on Warm Ivory (`#FBF6F3`): **10.04 : 1** (WCAG AAA) / **9.61 : 1** (WCAG AAA).
- **Card Surfaces (`--white`)**: `#FFFFFF` / `#FDFBF9` (Pure White with 8px radius and subtle ambient drop shadow).
- **Hairline Dividers & Borders (`--divider`)**: `#DDD7CF` / `rgba(24, 42, 61, 0.08)`.

## 2. Background Texture
- **Official Texture**: Soft paper noise filter with `background-blend-mode: soft-light` over `#FBF6F3` with soft ambient radial light blooms in Gold (`rgba(140, 103, 52, 0.12)`).

## 3. Typography
- **Headings & Display**: `'Marcellus', serif` (Weight 400, editorial architectural luxury)
- **Body & UI Elements**: `'Manrope', sans-serif` (Weights 400, 500, 600, 700)
- **Brand Logo**: `'Josefin Sans', sans-serif` (Weight 600)

## 4. Layout & Geometry
- **Container Widths**: Maximum container width is **1280px** with `2rem` side padding (`1216px` active content area) on Desktop, and `1rem` on Mobile.
- **Editorial Columns**: Reading copy and paragraph text should remain constrained to ~`760px` for optimal readability.
- **Corner Radius**: Unified **`8px`** (`border-radius: 8px`) across all cards, modals, buttons, and badges.
