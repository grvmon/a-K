import re

def update_css(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Typography
    content = content.replace("Cormorant Garamond", "Marcellus")
    content = content.replace("Josefin Sans", "Manrope")
    
    # Ensure headings don't have bold weight if they use Marcellus
    # (This is tricky with regex, we might just enforce 400 for Marcellus if we can, or just replace weights).
    content = re.sub(r'(font-family:\s*[\'"]?Marcellus[\'"]?[^;]*;[\s\S]*?font-weight:\s*)([56789]00|bold)', r'\g<1>400', content)

    # 2. Colors 
    # Not blindly replacing colors to avoid breaking things unexpectedly, 
    # but the style guide wants strict AAA compliance. Let's see what's in the CSS.
    
    # 3. Layout, Geometry & Shadows
    # Replace border-radius with 4px everywhere except 50% for circles
    content = re.sub(r'border-radius:\s*(?!50%)[^;]+;', 'border-radius: 4px;', content)
    
    # Replace box-shadow on cards with none (or just remove them)
    # We will remove generic box-shadows.
    # content = re.sub(r'box-shadow:\s*[^;]+;', 'box-shadow: none;', content)
    
    # Transitions
    content = re.sub(r'transition:\s*([^;]+);', lambda m: m.group(0).replace('0.3s', '0.4s').replace('0.2s', '0.4s'), content)

    with open(filepath, 'w') as f:
        f.write(content)


def update_html(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Lexicon replacements - careful not to hit classes/IDs or URLs.
    # We'll use lookarounds to try to only replace visible text.
    # A simple approach for HTML text replacement is parsing or careful regex.
    # Let's do careful regex outside of tags.
    
    def replace_text(match):
        text = match.group(1)
        # Lexicon map
        text = re.sub(r'\bBuy Now\b', 'Request Advisory Call', text, flags=re.IGNORECASE)
        # only replace Submit if it's visible text, not an attribute like type="submit"
        text = re.sub(r'\bSubmit\b', 'Get Buyer Analysis', text)
        text = re.sub(r'\bLuxury\b', 'Institutional-Grade', text, flags=re.IGNORECASE)
        text = re.sub(r'\bPremium\b', 'A-Grade', text, flags=re.IGNORECASE)
        text = re.sub(r'\bAmenities\b', 'Asset Fundamentals', text, flags=re.IGNORECASE)
        text = re.sub(r'\bFeatures\b', 'Township Infrastructure', text, flags=re.IGNORECASE)
        text = re.sub(r'\bPrice List\b', 'Valuation Matrix', text, flags=re.IGNORECASE)
        text = re.sub(r'\bBrochure\b', 'Asset Dossier', text, flags=re.IGNORECASE)
        return ">" + text + "<"

    content = re.sub(r'>([^<]+)<', replace_text, content)
    
    with open(filepath, 'w') as f:
        f.write(content)

update_css('website.css')
update_html('index.html')
print("Done")
