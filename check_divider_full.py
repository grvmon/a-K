import re

with open('website.css', 'r') as f:
    css = f.read()

# Find ALL rules mentioning brand-divider
matches = list(re.finditer(r'[^{}]*brand-divider[^{}]*\{[^}]*\}', css))
for m in matches:
    print("RULE:", m.group(0))
    print("---")
