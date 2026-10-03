import re
with open('index.html', 'r') as f:
    html = f.read()

m = re.search(r'<div[^>]*luxury-approach-right[^>]*>(.*?)</div>\s*</div>\s*</div>\s*</section>', html, re.DOTALL)
if m:
    print(m.group(1)[:500])
