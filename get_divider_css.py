import re

with open('website.css', 'r') as f:
    css = f.read()

for cls in ['.brand-divider', '.editorial-divider']:
    m = re.findall(r'(' + cls.replace('.', r'\.') + r'\s*\{[^}]*})', css)
    if m:
        for match in m:
            print(match)
            
print("--- Inline ---")
with open('index.html', 'r') as f:
    html = f.read()

styles = re.findall(r'<style>(.*?)</style>', html, flags=re.DOTALL)
if styles:
    inline_css = styles[0]
    for cls in ['.brand-divider', '.editorial-divider']:
        m = re.findall(r'(' + cls.replace('.', r'\.') + r'\s*\{[^}]*})', inline_css)
        if m:
            for match in m:
                print(match)
