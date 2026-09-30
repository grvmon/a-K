import re

with open('website.css', 'r') as f:
    css = f.read()

# 1. Fix Hover Color
css = re.sub(r'background:\s*linear-gradient\(135deg,\s*var\(--highlight-peach\)\s*0%,\s*var\(--highlight-peach\)\s*100%\)\s*!important\s*;?', 'background: var(--text-copper-aaa) !important;', css)

# 2. Fix Physical Lift (translateY(-1px))
css = re.sub(r'transform:\s*translateY\(-1px\)(?:\s*!important)?\s*;?', '', css)
css = re.sub(r'transform:\s*scale\(1\.02\)\s*translateY\(-1px\)(?:\s*!important)?\s*;?', 'transform:scale(1.02);', css)

# 3. Force Transparent Header CTA to actually be transparent
# Let's just append an overriding rule at the VERY END of the file to guarantee it wins.
ultimate_cta_rules = """
/* ULTIMATE CTA TRANSPARENCY FIX */
.header-nav.transparent-header:not(.scrolled) .nav-cta-btn {
    background: transparent !important;
    border: 0.5px solid rgba(255, 255, 255, 0.4) !important;
    color: #FFFFFF !important;
    box-shadow: none !important;
}
.header-nav.transparent-header:not(.scrolled) .nav-cta-btn:hover {
    background: rgba(255, 255, 255, 0.1) !important;
    color: #FFFFFF !important;
}
"""
if "ULTIMATE CTA TRANSPARENCY FIX" not in css:
    css += ultimate_cta_rules

with open('website.css', 'w') as f:
    f.write(css)

