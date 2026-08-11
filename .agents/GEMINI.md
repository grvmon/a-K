# Acre & Key Brand & Design Guidelines (Official Style Guide)
Reference: https://aabhisrv.github.io/ackey/style-guide/

## 1. Master Color Palette (Locked & Permanent)
- **Antique Brass / Refined Brass (`--refined-brass`)**: `#9A7B4F` (`rgba(154, 123, 79, ...)`)
  - Used for: All primary CTA buttons (`.sd-btn-gold`), timeline step numbers (01–04), active progress traces, key italic accents, badges, and icon highlights.
- **Warm Ivory Canvas Base (`--warm-ivory`)**: `#FBF6F3`
  - Used for: 75% site background canvas with subtle `soft-light` paper noise texture. Provides clean, soft ivory warmth. Zero grid lines, zero blueprint drawings, zero tint gradients.
- **Deep Navy (`--deep-navy` / `--deep-navy-100`)**: `rgba(24, 42, 61, 0.84)` / `#182A3D`
  - Used for: All primary titles, H1–H4 headings, 1-line Summary Banner boxes, mobile drawer headers, and site footer foundation.
- **Card Surfaces (`--white`)**: `#FFFFFF` / `#FDFBF9` (Pure White with 8px radius and subtle ambient drop shadow).
- **Supporting Neutrals**:
  - Dark Brass Accent: `#82643A`
  - Charcoal Body Text: `#222222` / `rgba(24, 42, 61, 0.84)`
  - Slate Gray (Subtitles/Meta): `#6B7280` / `#4B5563`
  - Warm Stone (Pill tags): `#EDE8E2`
  - Hairline Dividers & Borders: `#DDD7CF` / `rgba(24, 42, 61, 0.08)` / `rgba(154, 123, 79, 0.25)`

## 2. Background Texture
- **Official Texture**: Soft paper noise filter with `background-blend-mode: soft-light` over `#FBF6F3`.
- **Prohibited**: Heavy repeating grid crosshatches, yellow/navy full-viewport vertical tint gradients, or blueprint watermark sketches.

## 3. Typography
- **Headings & Display**: `'Marcellus', serif` (Weight 400, editorial architectural luxury)
- **Body & UI Elements**: `'Manrope', sans-serif` (Weights 400, 500, 600, 700)
- **Brand Logo**: `'Josefin Sans', sans-serif` (Weight 600)

## 4. Layout & Geometry
- **Container Widths**: Maximum container width is **1280px** with `2rem` side padding (`1216px` active content area).
- **Editorial Columns**: Reading copy and paragraph text should remain constrained to ~`760px` for optimal readability.
- **Corner Radius**: Unified **`8px`** (`border-radius: 8px`) across all cards, modals, buttons, and badges.
