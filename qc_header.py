import re

with open('website.css', 'r') as f:
    css = f.read()

def find_rule(selector):
    pattern = re.compile(re.escape(selector) + r'[^\{]*\{([^}]*)\}')
    match = pattern.search(css)
    if match:
        return match.group(1).strip()
    return None

print("brand-logo-text:", find_rule('.brand-logo-text'))
print("primary-cta-btn:", find_rule('.primary-cta-btn'))
print("header-nav:", find_rule('.header-nav:not(.transparent-header)'))
