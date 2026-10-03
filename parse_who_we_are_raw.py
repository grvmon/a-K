import re
with open('index.html', 'r') as f:
    html = f.read()

m = re.search(r'<section[^>]*who-were-for-section[^>]*>(.*?)</section>', html, re.DOTALL)
if m:
    print(m.group(1))

