import re

css_path = "/Users/gauravmongia/.gemini/antigravity/scratch/a-K/website.css"
css = open(css_path, "r").read()

# 1. Reduce section padding
css = re.sub(r'(\.micromarket-lens-section\s*\{[^}]*?padding-top:\s*)4rem;', r'\1 2rem;', css)
css = re.sub(r'(\.micromarket-lens-section\s*\{[^}]*?padding-bottom:\s*)4rem;', r'\1 2rem;', css)

# 2. Reduce grid margin
css = re.sub(r'(\.micromarket-grid\s*\{[^}]*?margin-bottom:\s*)2\.5rem;', r'\1 1rem;', css)

# 3. Reduce card padding
css = re.sub(r'(\.corridor-card\s*\{[^}]*?padding:\s*)1rem 1\.25rem;', r'\1 0.75rem 1rem;', css)

# 4. Reduce stack gap
css = re.sub(r'(\.micromarket-stack\s*\{[^}]*?gap:\s*)0\.75rem;', r'\1 0.5rem;', css)

# 5. Reduce map min-height
css = re.sub(r'(\.micromarket-map-wrapper\s*\{[^}]*?min-height:\s*)480px;', r'\1 380px;', css)

# 6. Override section header specifically for this section by appending a rule
if '.micromarket-lens-section .section-header' not in css:
    css += "\n\n/* Compact Fold Override */\n.micromarket-lens-section .section-header { margin-bottom: 1.5rem !important; }\n"

open(css_path, "w").write(css)
print("Updated CSS to fit 1 fold.")
