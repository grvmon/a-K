import re

with open('website.css', 'r') as f:
    css = f.read()

# Grab all sections
with open('index.html', 'r') as f:
    html = f.read()

sections = re.findall(r'<section([^>]+)>', html)
for i, attrs in enumerate(sections):
    id_m = re.search(r'id=[\'"]?([^\s\'">]+)', attrs)
    class_m = re.search(r'class=[\'"]([^\'"]+)[\'"]', attrs)
    id_val = id_m.group(1) if id_m else ''
    class_val = class_m.group(1) if class_m else ''
    
    classes = class_val.split()
    
    bg = "Inherits Body: var(--warm-ivory)"
    for cls in classes:
        m = re.search(r'\.' + cls + r'\s*\{[^}]*?background(?:-color)?\s*:\s*([^;}!]+)', css, re.IGNORECASE)
        if m:
            bg = m.group(1).strip()
    if id_val:
        m = re.search(r'#' + id_val + r'\s*\{[^}]*?background(?:-color)?\s*:\s*([^;}!]+)', css, re.IGNORECASE)
        if m:
            bg = m.group(1).strip()
            
    print(f"Section: {id_val or class_val} | Background: {bg}")

# Footer
footer = re.search(r'<footer([^>]+)>', html)
if footer:
    attrs = footer.group(1)
    class_m = re.search(r'class=[\'"]([^\'"]+)[\'"]', attrs)
    if class_m:
        classes = class_m.group(1).split()
        bg = "Inherits Body: var(--warm-ivory)"
        for cls in classes:
            m = re.search(r'\.' + cls + r'\s*\{[^}]*?background(?:-color)?\s*:\s*([^;}!]+)', css, re.IGNORECASE)
            if m:
                bg = m.group(1).strip()
        print(f"Footer | Background: {bg}")

