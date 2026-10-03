import re

with open('website.css', 'r') as f:
    css = f.read()

# Look for borders on sections
print("--- Section Borders ---")
matches = re.findall(r'(\.[a-zA-Z0-9_-]*section[a-zA-Z0-9_-]*\s*\{[^}]*border[^:]*:\s*[^;}!]+)', css)
for m in set(matches):
    print(m)

# Also check hr tags and dividers
print("\n--- HR and Divider Classes ---")
dividers = re.findall(r'(\.divider[a-zA-Z0-9_-]*\s*\{[^}]*})', css)
for d in set(dividers):
    print(d)

hr = re.findall(r'(hr\s*\{[^}]*})', css)
for h in set(hr):
    print(h)
    
