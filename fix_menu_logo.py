import re
with open('website.css', 'r') as f:
    content = f.read()

# Remove text-transform: uppercase from menu links
content = re.sub(r'text-transform:\s*uppercase\s*!important;', '', content)
content = re.sub(r'text-transform:\s*uppercase\s*;', '', content)

with open('website.css', 'w') as f:
    f.write(content)
