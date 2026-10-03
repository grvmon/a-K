with open('index.html', 'r') as f:
    html = f.read()
import re
scripts = re.findall(r'<script.*?>(.*?)</script>', html, flags=re.DOTALL)
for s in scripts:
    if 'kicker' in s.lower() or 'hero-content' in s.lower():
        print(s[:500])
