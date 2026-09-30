import re

with open('website.css', 'r') as f:
    css = f.read()

# SAFE border-radius
css = re.sub(r'border-radius:[^\n;]+(;|(?=\n))', 'border-radius: 4px;', css)

# SAFE box-shadow (only match on the same line)
css = re.sub(r'box-shadow:[^\n;]+(;|(?=\n))', 'box-shadow: none;', css)

# Transitions
css = re.sub(r'transition:\s*([^;\n]+)(;|(?=\n))', lambda m: m.group(0).replace('0.3s', '0.4s').replace('0.2s', '0.4s').replace('0.5s', '0.4s'), css)

# Logo font
css = re.sub(r'--font-logo:\s*[\'"]?Manrope[\'"]?(;|(?=\n))', "--font-logo:'Josefin Sans';", css)

# Fix Menu Style: remove uppercase and heavy letter-spacing
def clean_nav_links(match):
    block = match.group(0)
    block = re.sub(r'text-transform:\s*uppercase\s*!important;', '', block)
    block = re.sub(r'text-transform:\s*uppercase\s*(;|(?=\n))', '', block)
    block = re.sub(r'letter-spacing:\s*0\.2em\s*!important;', 'letter-spacing: 0.02em !important;', block)
    block = re.sub(r'letter-spacing:\s*0\.12em\s*(;|(?=\n))', 'letter-spacing: 0.02em;', block)
    block = re.sub(r'letter-spacing:\s*0\.1em\s*!important;', 'letter-spacing: 0.02em !important;', block)
    block = re.sub(r'font-size:\s*12px\s*!important;', 'font-size: 14px !important;', block)
    block = re.sub(r'font-weight:\s*600\s*!important;', 'font-weight: 500 !important;', block)
    return block

css = re.sub(r'\.nav-links\s*a\s*\{[^}]*\}', clean_nav_links, css)

# Scrolled CTA rule
scrolled_rule = """
.header-nav.scrolled .nav-cta-btn {
    background: transparent !important;
    border: 0.5px solid rgba(255, 255, 255, 0.4) !important;
    color: #ffffff !important;
}
.header-nav.scrolled .nav-cta-btn:hover {
    border-color: #ffffff !important;
    background: rgba(255, 255, 255, 0.1) !important;
}
"""
if ".header-nav.scrolled .nav-cta-btn {" not in css:
    css += scrolled_rule

# Dark header CTA rule
dark_header_rule = """
.header-nav:not(.transparent-header) .nav-cta-btn,
body.property-page .header-nav .nav-cta-btn,
body.page-404 .header-nav .nav-cta-btn {
    background: transparent !important;
    border: 0.5px solid rgba(255, 255, 255, 0.4) !important;
    color: #ffffff !important;
}
.header-nav:not(.transparent-header) .nav-cta-btn:hover,
body.property-page .header-nav .nav-cta-btn:hover,
body.page-404 .header-nav .nav-cta-btn:hover {
    border-color: #ffffff !important;
    background: rgba(255, 255, 255, 0.1) !important;
}
"""
if ".header-nav:not(.transparent-header) .nav-cta-btn {" not in css:
    css += dark_header_rule

with open('website.css', 'w') as f:
    f.write(css)

# Update index.html
with open('index.html', 'r') as f:
    html = f.read()

def replace_text(match):
    text = match.group(1)
    text = re.sub(r'\bBuy Now\b', 'Request Advisory Call', text, flags=re.IGNORECASE)
    text = re.sub(r'\bSubmit\b', 'Get Buyer Analysis', text)
    text = re.sub(r'\bLuxury\b', 'Institutional-Grade', text, flags=re.IGNORECASE)
    text = re.sub(r'\bPremium\b', 'A-Grade', text, flags=re.IGNORECASE)
    text = re.sub(r'\bAmenities\b', 'Asset Fundamentals', text, flags=re.IGNORECASE)
    text = re.sub(r'\bFeatures\b', 'Township Infrastructure', text, flags=re.IGNORECASE)
    text = re.sub(r'\bPrice List\b', 'Valuation Matrix', text, flags=re.IGNORECASE)
    text = re.sub(r'\bBrochure\b', 'Asset Dossier', text, flags=re.IGNORECASE)
    return ">" + text + "<"

scripts = []
styles = []
def script_repl(m):
    scripts.append(m.group(0))
    return f"<!--SCRIPT_BLOCK_{len(scripts)-1}-->"
def style_repl(m):
    styles.append(m.group(0))
    return f"<!--STYLE_BLOCK_{len(styles)-1}-->"

html = re.sub(r'<script[^>]*>.*?</script>', script_repl, html, flags=re.DOTALL)
html = re.sub(r'<style[^>]*>.*?</style>', style_repl, html, flags=re.DOTALL)
html = re.sub(r'>([^<]+)<', replace_text, html)

for i, script in enumerate(scripts):
    html = html.replace(f"<!--SCRIPT_BLOCK_{i}-->", script)
for i, style in enumerate(styles):
    html = html.replace(f"<!--STYLE_BLOCK_{i}-->", style)

html = html.replace('class="nav-cta-btn primary-cta-btn"', 'class="nav-cta-btn"')

if 'Josefin+Sans' not in html:
    html = html.replace('family=Manrope', 'family=Josefin+Sans:wght@300;400;600;700&family=Manrope')

with open('index.html', 'w') as f:
    f.write(html)
