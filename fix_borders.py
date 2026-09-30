import re

def fix_borders(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Replace 1px solid with 0.5px solid for borders
    content = re.sub(r'border([^:]*):\s*1px\s+solid', r'border\1: 0.5px solid', content)
    # also handle border-bottom, border-top, etc.
    content = re.sub(r'border([^:]*):\s*(var\([^)]+\)|rgba?\([^)]+\)|#[0-9a-fA-F]+)\s+1px\s+solid', r'border\1: \2 0.5px solid', content)
    
    with open(filepath, 'w') as f:
        f.write(content)

fix_borders('website.css')
print("Done")
