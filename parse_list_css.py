import re
with open('website.css', 'r') as f:
    css = f.read()

matches = re.finditer(r'[^{}]*luxury-approach-list[^{}]*\{[^}]*\}', css)
for m in matches:
    print(m.group(0).strip())
    print("---")
    
matches = re.finditer(r'[^{}]*luxury-approach-right[^{}]*\{[^}]*\}', css)
for m in matches:
    print(m.group(0).strip())
    print("---")
