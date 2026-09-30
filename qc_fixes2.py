import re

with open('website.css', 'r') as f:
    content = f.read()

# 1. Fix typography: Cormorant Garamond -> Marcellus
content = content.replace("Cormorant Garamond", "Marcellus")
content = re.sub(r'(font-family:\s*[\'"]?Marcellus[\'"]?[^;]*;[\s\S]*?font-weight:\s*)([56789]00|bold)', r'\g<1>400', content)

# 2. Fix faux-italic/bold on highlight-brass and consultant-main-title
content = re.sub(r'(\.highlight-brass\s*\{[^}]*?)font-style:\s*italic\s*(;|(?=\n))', r'\1', content)
content = re.sub(r'(\.highlight-brass\s*\{[^}]*?)font-weight:\s*600\s*(;|(?=\n))', r'\1', content)
content = re.sub(r'(\.consultant-main-title\s*\{[^}]*?)font-weight:\s*600\s*(;|(?=\n))', r'\1', content)

# 3. Fix CTA hover contrast safely
content = re.sub(r'background:\s*linear-gradient\(135deg,\s*var\(--highlight-peach\)\s*0%,\s*var\(--highlight-peach\)\s*100%\)\s*!important;', 'background: var(--text-copper-aaa) !important;', content)

# 4. Remove physical lift on buttons
content = re.sub(r'transform:\s*translateY\(-1px\)\s*!important;', '', content)

# 5. Rule 13: Inline Link Behavior
inline_link_css = """
/* Rule 13: Inline Link Behavior */
p a, li a, .editorial-text a {
    color: var(--text-copper-aaa);
    text-decoration: underline;
    text-decoration-color: rgba(128,69,38,0.3);
    text-decoration-thickness: 1px;
    text-underline-offset: 4px;
    transition: text-decoration-color 0.4s ease;
}
p a:hover, li a:hover, .editorial-text a:hover {
    text-decoration-color: var(--text-copper-aaa);
}
"""
if "/* Rule 13: Inline Link Behavior */" not in content:
    content += inline_link_css

# 6. Fix Header/Footer Links Decoration
reset_css = """
/* Fix Header/Footer Links Decoration */
.header-nav .nav-links a, 
.header-nav .nav-links li a,
.mobile-drawer-nav a, 
.mobile-drawer-nav li a,
.site-footer a, 
.site-footer li a,
.nav-brand, .brand-logo-text {
    text-decoration: none !important;
    text-decoration-color: transparent !important;
}
"""
if "/* Fix Header/Footer Links Decoration */" not in content:
    content += reset_css

with open('website.css', 'w') as f:
    f.write(content)

with open('index.html', 'r') as f:
    html = f.read()

html = html.replace('class="hero-title Institutional-Grade-title"', 'class="hero-title premium-title"')
html = html.replace('class="hero-title A-Grade-title"', 'class="hero-title premium-title"')
html = html.replace('class="hero-kicker Institutional-Grade-kicker"', 'class="hero-kicker premium-kicker"')
html = html.replace('class="hero-kicker A-Grade-kicker"', 'class="hero-kicker premium-kicker"')
html = html.replace('class="hero-subtitle Institutional-Grade-subtitle"', 'class="hero-subtitle premium-subtitle"')
html = html.replace('class="hero-subtitle A-Grade-subtitle"', 'class="hero-subtitle premium-subtitle"')
html = html.replace('Institutional-Grade-inline-cta', 'premium-inline-cta')
html = html.replace('A-Grade-inline-cta', 'premium-inline-cta')
html = html.replace('Institutional-Grade-reveal', 'premium-reveal')
html = html.replace('A-Grade-reveal', 'premium-reveal')

with open('index.html', 'w') as f:
    f.write(html)
