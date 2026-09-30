import re

def update_css(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Colors (this might be risky if we just blindly replace hex codes, but we can replace variable definitions)
    # Let's find root variables and update them if they exist
    # If not, let's just make sure border-radius, transitions, and shadows are correct.
    
    # 1. Typography
    content = content.replace("Cormorant Garamond", "Marcellus")
    content = content.replace("Josefin Sans", "Manrope")
    
    # 2. Border-radius (skip 50% for circles)
    # Using a simple regex to replace border-radius values with 4px
    content = re.sub(r'border-radius:\s*(?!50%|0)[^;]+;', 'border-radius: 4px;', content)
    
    # 3. Transitions
    content = re.sub(r'transition:\s*([^;]+);', lambda m: m.group(0).replace('0.3s', '0.4s').replace('0.2s', '0.4s').replace('0.5s', '0.4s'), content)

    # 4. Box shadows (remove them except for popups if possible, but the user said except popups dont change for now).
    # Since popup CSS is mostly in abha-form.css and lead-form.css, we can just remove box-shadow from website.css.
    content = re.sub(r'box-shadow:\s*[^;]+;', 'box-shadow: none;', content)
    
    # 5. Font weights for Marcellus - this is harder with regex, but we can try to find font-weight next to Marcellus.
    # Instead, we'll just replace font-weight: 600/700 with 400 where it's for headings.
    # We can replace all font-weight: bold; with font-weight: 500; (Manrope) or 400.
    
    # Let's update root variables for colors
    content = re.sub(r'--cta-gradient:\s*[^;]+;', '--cta-gradient: linear-gradient(135deg, #be7555 0%, #9f5334 100%);', content)
    content = re.sub(r'--text-copper-aaa:\s*[^;]+;', '--text-copper-aaa: #804526;', content)
    content = re.sub(r'--highlight-peach:\s*[^;]+;', '--highlight-peach: #e5b899;', content)
    content = re.sub(r'--titanium-frost:\s*[^;]+;', '--titanium-frost: #FAFAFA;', content)
    content = re.sub(r'--obsidian-black:\s*[^;]+;', '--obsidian-black: #0A0A0B;', content)
    content = re.sub(r'--neutral-grey:\s*[^;]+;', '--neutral-grey: #55555A;', content)
    
    with open(filepath, 'w') as f:
        f.write(content)

def update_html(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # To safely replace text in HTML outside of tags and attributes, we can split by < and >
    parts = []
    in_tag = False
    
    # Simple state machine to split text nodes and tag nodes
    tokens = re.split(r'(<[^>]*>)', content)
    
    for token in tokens:
        if token.startswith('<'):
            # This is a tag, we do not replace lexicon inside tags EXCEPT if we want to replace classes?
            # User said no css used should be not as per style guide.
            # But the lexicon maps to text.
            parts.append(token)
        else:
            # Text node, safe to replace lexicon
            text = token
            text = re.sub(r'\bBuy Now\b', 'Request Advisory Call', text, flags=re.IGNORECASE)
            text = re.sub(r'\bSubmit\b', 'Get Buyer Analysis', text)
            text = re.sub(r'\bLuxury\b', 'Institutional-Grade', text, flags=re.IGNORECASE)
            text = re.sub(r'\bPremium\b', 'A-Grade', text, flags=re.IGNORECASE)
            text = re.sub(r'\bAmenities\b', 'Asset Fundamentals', text, flags=re.IGNORECASE)
            text = re.sub(r'\bFeatures\b', 'Township Infrastructure', text, flags=re.IGNORECASE)
            text = re.sub(r'\bPrice List\b', 'Valuation Matrix', text, flags=re.IGNORECASE)
            text = re.sub(r'\bBrochure\b', 'Asset Dossier', text, flags=re.IGNORECASE)
            parts.append(text)
            
    with open(filepath, 'w') as f:
        f.write(''.join(parts))

update_css('website.css')
update_html('index.html')
print("Done")
