import re
with open('website.css', 'r') as f:
    css = f.read()

# Remove translateY(-1px) with or without !important, with or without semicolon
css = re.sub(r'transform:\s*translateY\(-1px\)(?:\s*!important)?\s*;?', '', css)
css = re.sub(r'transform:\s*scale\(1\.02\)\s*translateY\(-1px\)(?:\s*!important)?\s*;?', 'transform:scale(1.02);', css)

with open('website.css', 'w') as f:
    f.write(css)

