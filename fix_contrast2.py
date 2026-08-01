import re

css_path = "/Users/gauravmongia/.gemini/antigravity/scratch/a-K/website.css"
css = open(css_path, "r").read()

# Fix --refined-brass to --dark-brass for text classes
gold_classes = [
    r'\.spider-node-num',
    r'\.spider-node-num,\s*\.market-lens-num',
    r'\.market-lens-num',
    r'\.gold-num',
    r'\.metric-val',
    r'\.testimonial-author',
    r'\.framework-card-sub'
]

for cls in gold_classes:
    # Match class block and replace refined-brass with dark-brass
    pattern = r'(' + cls + r'[^}]*?)color:\s*var\(--refined-brass\)'
    css = re.sub(pattern, r'\1color: var(--dark-brass)', css)

# Fix muted-slate + opacity to deep-slate
slate_classes = [
    r'\.framework-questions-header',
    r'\.framework-card-sub',
    r'em',
    r'\.metric-label'
]

for cls in slate_classes:
    # Replace muted-slate with deep-slate and remove opacity if exists
    # First just replace the color
    pattern = r'(' + cls + r'[^}]*?)color:\s*var\(--muted-slate\)'
    css = re.sub(pattern, r'\1color: var(--deep-slate)', css)
    # Then remove opacity
    pattern_op = r'(' + cls + r'[^}]*?)\s*opacity:\s*0\.\d+;'
    css = re.sub(pattern_op, r'\1', css)
    
# Footer badge span
css = re.sub(r'(\.footer-badge\s*\{[^}]*?)color:\s*var\(--muted-slate\)', r'\1color: var(--deep-slate)', css)

open(css_path, "w").write(css)
print("Updated CSS with robust regex.")
