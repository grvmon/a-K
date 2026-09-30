import re

with open('website.css', 'r') as f:
    css = f.read()

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

