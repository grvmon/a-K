import re
with open('website.css', 'r') as f:
    content = f.read()

# Remove comments
content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
# Remove extra whitespace but keep a single space to avoid breaking things like 'and (max-width'
content = re.sub(r'\s+', ' ', content)
# Safe stripping: remove spaces around {} but only if it's safe
content = content.replace(' {', '{').replace('{ ', '{')
content = content.replace(' }', '}').replace('} ', '}')

with open('website.min.css', 'w') as f:
    f.write(content)
