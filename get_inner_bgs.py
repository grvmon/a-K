import re

with open('index.html', 'r') as f:
    html = f.read()

# I will just grep the HTML for background inline styles or specific wrapper classes
wrappers = re.findall(r'class="([^"]*wrapper[^"]*|[^"]*container[^"]*|[^"]*inner[^"]*)"', html)
for w in set(wrappers):
    print("Found wrapper class:", w)
