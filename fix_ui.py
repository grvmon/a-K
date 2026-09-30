import re

# 1. Update index.html
with open('index.html', 'r') as f:
    html = f.read()

# Remove .primary-cta-btn from the header nav CTA
# In index.html: <a href="#" class="nav-cta-btn primary-cta-btn"
html = html.replace('class="nav-cta-btn primary-cta-btn"', 'class="nav-cta-btn"')

# Ensure Google Fonts link has Josefin Sans (it should already be there from fix_logo.py)
if 'Josefin+Sans' not in html:
    html = html.replace('family=Manrope', 'family=Josefin+Sans:wght@300;400;600;700&family=Manrope')

with open('index.html', 'w') as f:
    f.write(html)

# 2. Update website.css
with open('website.css', 'r') as f:
    css = f.read()

# Fix logo font if not already done
css = re.sub(r'--font-logo:\s*[\'"]?Manrope[\'"]?;', "--font-logo:'Josefin Sans';", css)

# Fix Menu Style: remove uppercase and letter-spacing from .nav-links a
# Let's find .nav-links a { ... } and remove text-transform and letter-spacing
def clean_nav_links(match):
    block = match.group(0)
    block = re.sub(r'text-transform:\s*uppercase\s*!important;', '', block)
    block = re.sub(r'text-transform:\s*uppercase\s*;', '', block)
    block = re.sub(r'letter-spacing:\s*0\.2em\s*!important;', 'letter-spacing: 0.02em !important;', block)
    block = re.sub(r'letter-spacing:\s*0\.12em\s*;', 'letter-spacing: 0.02em;', block)
    block = re.sub(r'letter-spacing:\s*0\.1em\s*!important;', 'letter-spacing: 0.02em !important;', block)
    # Also adjust font-size to be a bit larger since we removed uppercase and heavy letter spacing
    block = re.sub(r'font-size:\s*12px\s*!important;', 'font-size: 14px !important;', block)
    # Adjust font-weight to 500 for a cleaner look
    block = re.sub(r'font-weight:\s*600\s*!important;', 'font-weight: 500 !important;', block)
    return block

css = re.sub(r'\.nav-links\s*a\s*\{[^}]*\}', clean_nav_links, css)

with open('website.css', 'w') as f:
    f.write(css)

