import re

with open('website.css', 'r') as f:
    css = f.read()

# 1. Remove the transparent header CTA fix
css = re.sub(r'/\* ULTIMATE CTA TRANSPARENCY FIX \*/.*?\}\s*\}?', '', css, flags=re.DOTALL)
css = re.sub(r'\.header-nav\.transparent-header:not\(\.scrolled\)\s*\.nav-cta-btn\s*\{[^}]*\}', '', css)
css = re.sub(r'\.header-nav\.scrolled\s*\.nav-cta-btn\s*\{[^}]*\}', '', css)
css = re.sub(r'\.header-nav\.scrolled\s*\.nav-cta-btn:hover\s*\{[^}]*\}', '', css)
css = re.sub(r'\.header-nav:not\(\.transparent-header\)\s*\.nav-cta-btn\s*\{[^}]*\}', '', css)
css = re.sub(r'body\.property-page.*?\.nav-cta-btn:hover\s*\{[^}]*\}', '', css)
css = re.sub(r'body\.page-404.*?\.nav-cta-btn:hover\s*\{[^}]*\}', '', css)

# 2. Restore Hover Effect to Peach Gradient, but with BLACK text for WCAG AAA
css = re.sub(r'background:\s*var\(--text-copper-aaa\)\s*!important;', 'background: linear-gradient(135deg, var(--highlight-peach) 0%, var(--highlight-peach) 100%) !important;', css)

# Add explicit color changes for hover state to ensure black text
hover_text_css = """
/* CTA Hover WCAG AAA Contrast Fix */
.primary-cta-btn:hover, .nav-cta-btn:hover, .mobile-drawer-cta:hover, .premium-inline-cta:hover {
    color: var(--obsidian-black) !important;
}
.primary-cta-btn:hover span, .nav-cta-btn:hover span, .mobile-drawer-cta:hover span, .premium-inline-cta:hover span {
    color: var(--obsidian-black) !important;
}
.primary-cta-btn:hover .cta-arrow-badge, .nav-cta-btn:hover .cta-arrow-badge, .mobile-drawer-cta:hover .cta-arrow-badge, .premium-inline-cta:hover .cta-arrow-badge {
    border-color: var(--obsidian-black) !important;
    background: transparent !important;
}
.primary-cta-btn:hover .cta-arrow-badge svg, .nav-cta-btn:hover .cta-arrow-badge svg, .mobile-drawer-cta:hover .cta-arrow-badge svg, .premium-inline-cta:hover .cta-arrow-badge svg {
    stroke: var(--obsidian-black) !important;
}
"""
if "/* CTA Hover WCAG AAA Contrast Fix */" not in css:
    css += hover_text_css

# 3. Restore arrow badge border-radius to 50%
css = re.sub(r'(\.cta-arrow-badge\s*\{[^}]*?)border-radius:\s*4px;', r'\1border-radius: 50%;', css)

with open('website.css', 'w') as f:
    f.write(css)

