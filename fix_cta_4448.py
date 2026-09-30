import re

with open('website.css', 'r') as f:
    css = f.read()

# Remove transparent override
css = re.sub(r'\.header-nav\s*\.nav-cta-btn\s*\{[^}]*\}', '', css)
css = re.sub(r'\.header-nav\s*\.nav-cta-btn:hover\s*\{[^}]*\}', '', css)

with open('website.css', 'w') as f:
    f.write(css)

