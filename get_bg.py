import re

with open('website.css', 'r') as f:
    css = f.read()

def find_bg(selector):
    pattern = re.compile(selector.replace('.', r'\.') + r'\s*\{[^}]*?background(?:-color)?\s*:\s*([^;}!]+)', re.IGNORECASE)
    matches = pattern.findall(css)
    if matches:
        return matches[-1].strip()
    return "Not found"

selectors = [
    '.premium-dark-hero',
    '.hero-section',
    '.luxury-approach-section',
    '.who-were-for-section',
    '.framework-section',
    '#core',
    '.core-section',
    '#about-us',
    '.about-section',
    '#testimonials',
    '.testimonials-section',
    '.consultant-info-section',
    '.site-footer',
    'footer'
]

for s in selectors:
    print(f"{s}: {find_bg(s)}")
