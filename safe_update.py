import re

with open('website.css', 'r') as f:
    content = f.read()

# Replace border-radius with 4px everywhere except 50% for circles and 0 for straight edges
content = re.sub(r'border-radius:\s*(?!50%|0)[^;]+;', 'border-radius: 4px;', content)

# Remove generic box-shadows on CARDS ONLY to avoid deleting structural shadows!
# The problem was we deleted box-shadow globally without matching the semicolon properly!
# Let's just remove box shadows that have a semicolon.
# BE VERY CAREFUL: [^;]+ matches everything until the FIRST semicolon, which might be lines away!
# Instead, match ONLY on the same line!
content = re.sub(r'box-shadow:[^\n;]+;', 'box-shadow: none;', content)

# Change transition speeds to 0.4s
content = re.sub(r'transition:\s*([^;]+);', lambda m: m.group(0).replace('0.3s', '0.4s').replace('0.2s', '0.4s').replace('0.5s', '0.4s'), content)

with open('website.css', 'w') as f:
    f.write(content)

with open('index.html', 'r') as f:
    html = f.read()
    
# Apply the Lexicon rule ONLY to text nodes in HTML, avoiding <style> and <script> tags!
# Easiest way: just regex outside of ANY tag, and ALSO manually skip <style>...</style> and <script>...</script>.
def replace_text(match):
    text = match.group(1)
    text = re.sub(r'\bBuy Now\b', 'Request Advisory Call', text, flags=re.IGNORECASE)
    text = re.sub(r'\bSubmit\b', 'Get Buyer Analysis', text)
    text = re.sub(r'\bLuxury\b', 'Institutional-Grade', text, flags=re.IGNORECASE)
    text = re.sub(r'\bPremium\b', 'A-Grade', text, flags=re.IGNORECASE)
    text = re.sub(r'\bAmenities\b', 'Asset Fundamentals', text, flags=re.IGNORECASE)
    text = re.sub(r'\bFeatures\b', 'Township Infrastructure', text, flags=re.IGNORECASE)
    text = re.sub(r'\bPrice List\b', 'Valuation Matrix', text, flags=re.IGNORECASE)
    text = re.sub(r'\bBrochure\b', 'Asset Dossier', text, flags=re.IGNORECASE)
    return ">" + text + "<"

# First, extract out style and script blocks so they don't get touched
scripts = []
styles = []
def script_repl(m):
    scripts.append(m.group(0))
    return f"<!--SCRIPT_BLOCK_{len(scripts)-1}-->"
def style_repl(m):
    styles.append(m.group(0))
    return f"<!--STYLE_BLOCK_{len(styles)-1}-->"

html = re.sub(r'<script[^>]*>.*?</script>', script_repl, html, flags=re.DOTALL)
html = re.sub(r'<style[^>]*>.*?</style>', style_repl, html, flags=re.DOTALL)

# Now replace lexicon
html = re.sub(r'>([^<]+)<', replace_text, html)

# Put them back
for i, script in enumerate(scripts):
    html = html.replace(f"<!--SCRIPT_BLOCK_{i}-->", script)
for i, style in enumerate(styles):
    html = html.replace(f"<!--STYLE_BLOCK_{i}-->", style)

with open('index.html', 'w') as f:
    f.write(html)
