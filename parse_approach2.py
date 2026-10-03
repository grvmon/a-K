import re

with open('index.html', 'r') as f:
    html = f.read()

m = re.search(r'<section[^>]*luxury-approach-section[^>]*>(.*?)</section>', html, re.DOTALL)
if m:
    content = m.group(1)
    
    titles = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', content)
    print("Titles:", titles)
    
    item_titles = re.findall(r'<h4[^>]*class=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</h4>', content)
    print("Item Titles:", item_titles)
    
    paragraphs = re.findall(r'<p[^>]*class=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</p>', content)
    for p in paragraphs[:2]:
        print("Para:", p[0], p[1][:100])
