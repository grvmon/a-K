import re
with open('index.html', 'r') as f:
    html = f.read()

m = re.search(r'<section[^>]*luxury-approach-section[^>]*>(.*?)</section>', html, re.DOTALL)
if m:
    content = m.group(1)
    # Check for grid classes
    print("Has luxury-approach-grid?", 'luxury-approach-grid' in content)
    print("Has luxury-approach-left?", 'luxury-approach-left' in content)
    print("Has luxury-approach-right?", 'luxury-approach-right' in content)
    
    # Extract the img wrapper
    img = re.search(r'<div[^>]*luxury-approach-img-wrapper[^>]*>(.*?)</div>', content, re.DOTALL)
    if img:
        print("IMG HTML:", img.group(0)[:200])

