import re

with open('index.html', 'r') as f:
    html = f.read()

styles = re.findall(r'<style>(.*?)</style>', html, flags=re.DOTALL)
if styles:
    inline_css = styles[0]
else:
    inline_css = ""

print("--- Inline Section Borders ---")
matches = re.findall(r'(\.[a-zA-Z0-9_-]*section[a-zA-Z0-9_-]*\s*\{[^}]*border[^:]*:\s*[^;}!]+)', inline_css)
for m in set(matches):
    print(m)

print("\n--- Inline HR and Divider Classes ---")
dividers = re.findall(r'(\.divider[a-zA-Z0-9_-]*\s*\{[^}]*})', inline_css)
for d in set(dividers):
    print(d)

hr = re.findall(r'(hr\s*\{[^}]*})', inline_css)
for h in set(hr):
    print(h)

# Check if there are any border properties applied directly via style="" on section tags
print("\n--- HTML style attributes ---")
inline_styles = re.findall(r'<section[^>]*style=[\'"]([^\'"]*border[^\'"]*)[\'"]', html)
for s in inline_styles:
    print(s)

