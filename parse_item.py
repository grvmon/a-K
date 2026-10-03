import re
with open('index.html', 'r') as f:
    html = f.read()

items = re.findall(r'<div[^>]*class="luxury-approach-item[^"]*"[^>]*>(.*?)</div>', html, re.DOTALL)
if items:
    print(items[0][:500])
