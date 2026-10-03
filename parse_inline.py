import re
with open('index.html', 'r') as f:
    html = f.read()

styles = re.findall(r'<style>(.*?)</style>', html, flags=re.DOTALL)
if styles:
    inline_css = styles[0]
    matches = re.findall(r'(\.section-title\s*\{[^}]*})', inline_css)
    for m in matches:
        print(m)
