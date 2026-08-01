import re

css_path = "/Users/gauravmongia/.gemini/antigravity/scratch/a-K/website.css"
css = open(css_path, "r").read()

# 1. Update button text color from --white to --deep-navy
css = re.sub(r'(\.sd-btn-gold\s*\{[^}]*?color:\s*)var\(--white\)', r'\1var(--deep-navy)', css)
css = re.sub(r'(\.cookie-btn-accept\s*\{[^}]*?color:\s*)var\(--white\)', r'\1var(--deep-navy)', css)

# 2. Update gold text from --refined-brass to --dark-brass
css = re.sub(r'(\.spider-node-num,\s*\.market-lens-num\s*\{[^}]*?color:\s*)var\(--refined-brass\)', r'\1var(--dark-brass)', css)
css = re.sub(r'(\.gold-num\s*\{[^}]*?color:\s*)var\(--refined-brass\)', r'\1var(--dark-brass)', css)
# .metric-val is slightly trickier, let's find color: var(--refined-brass) within metric-val blocks
css = re.sub(r'(\.metric-val\s*\{[^}]*?color:\s*)var\(--deep-navy\)', r'\1var(--deep-navy)', css) # Actually metric-val is deep navy? Wait, I should just replace specific blocks.

# Muted text opacity removal and dark slate
# .testimonial-author
css = re.sub(r'(\.testimonial-author\s*\{[^}]*?)color:\s*var\(--muted-slate\);\s*opacity:\s*0\.8;', r'\1color: var(--deep-slate);', css)
css = re.sub(r'(\.framework-card-sub\s*\{[^}]*?)color:\s*var\(--muted-slate\);\s*opacity:\s*0\.85;', r'\1color: var(--deep-slate);', css)

# Fallback: Just blanket replace opacity in specific classes if needed, but safer to use replace()
open(css_path, "w").write(css)
print("Updated CSS via regex.")
