import re
with open('index.html', 'r') as f:
    html = f.read()

styles = re.findall(r'<style>(.*?)</style>', html, flags=re.DOTALL)
if styles:
    inline_css = styles[0]
else:
    inline_css = ""

def find_bg(selector):
    pattern = re.compile(selector.replace('.', r'\.') + r'\s*\{[^}]*?background(?:-color)?\s*:\s*([^;}!]+)', re.IGNORECASE)
    matches = pattern.findall(inline_css)
    if matches:
        return matches[-1].strip()
    return "Not found"

selectors = [
    '.premium-dark-hero', '.hero-section', '.luxury-approach-section',
    '.who-were-for-section', '.framework-section', '#core', '#about-us', 
    '#testimonials', '.consultant-info-section', '.site-footer',
    '.about-us-section', '.core-values-section', '.testimonials-container'
]

for s in selectors:
    print(f"{s}: {find_bg(s)}")
