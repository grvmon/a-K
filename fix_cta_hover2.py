import re

def fix_css(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Replace specific string
    target = "background: linear-gradient(135deg, var(--highlight-peach) 0%, var(--highlight-peach) 100%) !important;"
    replacement = "background: var(--text-copper-aaa) !important;"
    content = content.replace(target, replacement)
    
    # Just in case there are spacing differences:
    content = re.sub(r'background:\s*linear-gradient\(135deg,\s*var\(--highlight-peach\)\s*0%,\s*var\(--highlight-peach\)\s*100%\)\s*!important;', replacement, content)

    with open(filepath, 'w') as f:
        f.write(content)

fix_css('website.css')
print("Done")
