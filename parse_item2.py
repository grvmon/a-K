import re
with open('index.html', 'r') as f:
    html = f.read()

m = re.search(r'class="luxury-approach-item[^"]*"(.*?)</p>', html, re.DOTALL)
if m:
    print(m.group(1))
