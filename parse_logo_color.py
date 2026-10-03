import re
with open('website.css', 'r') as f:
    css = f.read()

for m in re.finditer(r'[^{}]*brand-logo-text[^{}]*\{[^}]*\}', css):
    print(m.group(0).strip())
    print("---")
for m in re.finditer(r'[^{}]*nav-links\s*a[^{}]*\{[^}]*\}', css):
    print(m.group(0).strip())
    print("---")
