import os
import re

file_path = "/Users/patidar/Desktop/AnK website/home-loan-emi-calculator/index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove local body background
content = re.sub(r'body\s*\{\s*background-color:\s*#F8F9FA;\s*\}', '', content)

# Replace variables
content = content.replace('var(--ak-navy)', 'var(--deep-navy-100)')
content = content.replace('var(--ak-gold)', 'var(--refined-brass)')
content = content.replace('var(--ak-slate)', 'var(--deep-slate)')
content = content.replace('var(--ak-slate-light)', 'var(--muted-slate)')

# Replace hardcoded colors
content = content.replace('#182A3D', 'var(--deep-navy-100)')
content = content.replace('#D4AF37', 'var(--refined-brass)')
content = content.replace('#8B6508', 'var(--highlight-gold)')
content = content.replace('#1E232B', 'var(--deep-navy-100)')

# Replace border-radius
content = content.replace('border-radius: 16px;', 'border-radius: 8px;')
content = content.replace('border-radius: 12px;', 'border-radius: 8px;')

# Replace wrapper sizing
content = content.replace('max-width: 1200px;', 'max-width: 1280px;')
content = content.replace('padding: 0 1.5rem;', 'padding: 0 2rem;')

# Fonts
content = content.replace("font-family: 'Marcellus', serif;", "font-family: var(--font-heading);")
content = content.replace("font-family: 'Manrope', sans-serif;", "font-family: var(--font-body);")

# Backgrounds matching ivory
# The left panel had #FFFFFF. Let's keep it white as per guidelines: Card Surfaces (--white): #FFFFFF
# The trust badge header had #FDF9F3. We can keep it or use var(--warm-ivory)
content = content.replace('background: #FDF9F3;', 'background: var(--warm-ivory);')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
