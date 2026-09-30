import re

with open('website.css', 'r') as f:
    css = f.read()

# Make sure we have a proper rule for the scrolled CTA button
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

with open('website.css', 'w') as f:
    f.write(css)

