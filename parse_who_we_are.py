import re
with open('index.html', 'r') as f:
    html = f.read()

m = re.search(r'<section[^>]*who-were-for-section[^>]*>(.*?)</section>', html, re.DOTALL)
if m:
    content = m.group(1)
    # Extract the header text
    header = re.search(r'<div class="section-header.*?>(.*?)</div>', content, re.DOTALL)
    if header:
        print("--- HEADER ---")
        # Strip HTML tags
        print(re.sub(r'<[^>]+>', '', header.group(1)).strip())
    
    print("\n--- CARDS ---")
    cards = re.findall(r'<div class="framework-card[^>]*>(.*?)</div>\s*</div>', content, re.DOTALL)
    for i, c in enumerate(cards):
        # Extract title and text
        title = re.search(r'<h3 class="framework-card-title">(.*?)</h3>', c)
        text = re.search(r'<p class="framework-card-text">(.*?)</p>', c)
        print(f"Card {i+1}:")
        if title: print("Title:", title.group(1))
        if text: print("Text:", re.sub(r'<[^>]+>', '', text.group(1)).strip())
        print()

