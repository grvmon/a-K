import re
with open('website.css', 'r') as f:
    css = f.read()

matches = re.finditer(r'[^{}]*luxury-approach-item[^{}]*\{[^}]*\}', css)
for m in matches:
    print(m.group(0).strip())
    print("---")
