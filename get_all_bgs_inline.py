import re

with open('index.html', 'r') as f:
    html = f.read()

styles = re.findall(r'<style>(.*?)</style>', html, flags=re.DOTALL)
inline_css = styles[0] if styles else ""

sections = re.findall(r'<section([^>]+)>', html)
for i, attrs in enumerate(sections):
    id_m = re.search(r'id=[\'"]?([^\s\'">]+)', attrs)
    class_m = re.search(r'class=[\'"]([^\'"]+)[\'"]', attrs)
    id_val = id_m.group(1) if id_m else ''
    class_val = class_m.group(1) if class_m else ''
    
    classes = class_val.split()
    
    bg = None
    for cls in classes:
        m = re.search(r'\.' + cls + r'\s*\{[^}]*?background(?:-color)?\s*:\s*([^;}!]+)', inline_css, re.IGNORECASE)
        if m:
            bg = m.group(1).strip()
    if id_val:
        m = re.search(r'#' + id_val + r'\s*\{[^}]*?background(?:-color)?\s*:\s*([^;}!]+)', inline_css, re.IGNORECASE)
        if m:
            bg = m.group(1).strip()
            
    if bg:
        print(f"Section {id_val or class_val} INLINE override: {bg}")

# Footer
footer = re.search(r'<footer([^>]+)>', html)
if footer:
    attrs = footer.group(1)
    class_m = re.search(r'class=[\'"]([^\'"]+)[\'"]', attrs)
    if class_m:
        classes = class_m.group(1).split()
        for cls in classes:
            m = re.search(r'\.' + cls + r'\s*\{[^}]*?background(?:-color)?\s*:\s*([^;}!]+)', inline_css, re.IGNORECASE)
            if m:
                print(f"Footer INLINE override: {m.group(1).strip()}")

