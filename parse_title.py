import re
with open('index.html', 'r') as f:
    html = f.read()

m = re.search(r'<section[^>]*luxury-approach-section[^>]*>.*?The right home.*?</p>', html, re.DOTALL | re.IGNORECASE)
if m:
    print(m.group(0)[:400])
