import re

with open('index.html', 'r') as f:
    html = f.read()

# Extract sections
section_pattern = re.compile(r'<section([^>]+)>')
sections = section_pattern.findall(html)

for i, attrs in enumerate(sections):
    # try to extract id
    id_match = re.search(r'id=[\'"]?([^\s\'">]+)', attrs)
    id_val = id_match.group(1) if id_match else 'N/A'
    
    # try to extract class
    class_match = re.search(r'class=[\'"]([^\'"]+)[\'"]', attrs)
    class_val = class_match.group(1) if class_match else 'N/A'
    
    print(f"Section {i+1}: ID={id_val}, Class={class_val}")

print("\n--- FOOTER ---")
footer_pattern = re.compile(r'<footer([^>]+)>')
footer = footer_pattern.search(html)
if footer:
    attrs = footer.group(1)
    class_match = re.search(r'class=[\'"]([^\'"]+)[\'"]', attrs)
    class_val = class_match.group(1) if class_match else 'N/A'
    print(f"Footer: Class={class_val}")

