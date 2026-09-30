import re

def fix_faux(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Remove font-style: italic and font-weight: 600/700 from highlight-brass
    content = re.sub(r'(\.consultant-main-title \.highlight-brass \{[^}]*?)(font-style:\s*italic;\s*)([^}]*?\})', r'\1\3', content)
    content = re.sub(r'(\.consultant-main-title \.highlight-brass \{[^}]*?)(font-weight:\s*600;\s*)([^}]*?\})', r'\1font-weight: 400;\n\3', content)

    # General .highlight-brass
    content = re.sub(r'(\.highlight-brass \{[^}]*?)(font-style:\s*italic;\s*)([^}]*?\})', r'\1\3', content)
    
    # Check for other faux bolding on headings (Marcellus). We will just force all font-weight in headings to 400 where possible, or specifically in .highlight-brass and .brand-inline-text.
    content = re.sub(r'(\.brand-inline-text\s*\{[^}]*?)(font-style:\s*italic;\s*)([^}]*?\})', r'\1\3', content)

    # Make sure transition timings are 0.4s
    content = re.sub(r'transition:\s*border-color\s+0\.25s\s+ease,\s*box-shadow\s+0\.25s\s+ease', r'transition: border-color 0.4s ease, box-shadow 0.4s ease', content)

    with open(filepath, 'w') as f:
        f.write(content)

fix_faux('website.css')
print("Done")
