import re

with open('website.css', 'r') as f:
    content = f.read()

# Remove all @font-face blocks that mention 'Marcellus' or 'cormorant'
pattern = re.compile(r'@font-face\s*\{[^}]*\}', re.MULTILINE)
new_content = ""
last_end = 0

for match in pattern.finditer(content):
    block = match.group(0)
    if 'Marcellus' in block or 'cormorant' in block.lower():
        new_content += content[last_end:match.start()]
    else:
        new_content += content[last_end:match.end()]
    last_end = match.end()

new_content += content[last_end:]

with open('website.css', 'w') as f:
    f.write(new_content)
