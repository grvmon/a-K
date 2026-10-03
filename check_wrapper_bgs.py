import re

with open('website.css', 'r') as f:
    css = f.read()

classes = [
    'advisory-roadmap-container',
    'who-portfolio-wrapper',
    'framework-card-wrapper',
    'consultant-faq-linear-container',
    'luxury-approach-img-wrapper',
    'container',
    'who-card-inner'
]

for cls in classes:
    m = re.search(r'\.' + cls + r'\s*\{[^}]*?background(?:-color)?\s*:\s*([^;}!]+)', css, re.IGNORECASE)
    if m:
        print(f".{cls}: {m.group(1).strip()}")

