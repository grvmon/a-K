import re
with open('index.html', 'r') as f:
    html = f.read()

# find where the brand-divider is placed
matches = re.finditer(r'<hr[^>]*class="[^"]*divider[^"]*"[^>]*>|<div[^>]*class="[^"]*divider[^"]*"[^>]*>', html)
for m in matches:
    start = max(0, m.start() - 150)
    end = min(len(html), m.end() + 150)
    print("MATCH at", m.start())
    print(html[start:end])
    print("-" * 50)

