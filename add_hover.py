import re

with open('website.css', 'r') as f:
    css = f.read()

# Add hover effect for nav links
hover_rule = """
/* Added Luxury Hover Effect for Header Nav */
.header-nav .nav-links a:hover,
.header-nav .nav-links li a:hover {
    text-decoration: underline !important;
    text-decoration-color: #ffffff !important;
    text-decoration-thickness: 1px !important;
    text-underline-offset: 4px !important;
}
"""
if "/* Added Luxury Hover Effect for Header Nav */" not in css:
    css += hover_rule

with open('website.css', 'w') as f:
    f.write(css)

