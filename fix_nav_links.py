import re

def fix_css(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Ensure header links don't have underline
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

    with open(filepath, 'w') as f:
        f.write(content)

fix_css('website.css')
print("Done")
