import re
with open('index.html', 'r') as f:
    html = f.read()

m = re.search(r'<section[^>]*id=[\'"]?core[\'"]?[^>]*>(.*?)</section>', html, re.DOTALL)
if m:
    core_html = m.group(1)
    text = re.sub(r'<[^>]+>', ' ', core_html)
    text = re.sub(r'\s+', ' ', text)
    print(text[:300])
