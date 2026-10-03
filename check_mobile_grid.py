import re
with open('website.css', 'r') as f:
    css = f.read()

# find all occurrences of luxury-approach-grid
for i, line in enumerate(css.splitlines()):
    if 'luxury-approach-grid' in line:
        print(f"Line {i+1}: {line.strip()}")
