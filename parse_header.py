import re
with open('index.html', 'r') as f:
    html = f.read()

m = re.search(r'<header[^>]*>(.*?)</header>', html, re.DOTALL)
if m:
    print(m.group(0)[:1000])

