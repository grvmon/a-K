import re
with open('website.css', 'r') as f:
    content = f.read()

# Change --font-logo to Josefin Sans
content = re.sub(r'--font-logo:\s*[\'"]?[^\'"]+[\'"]?;', "--font-logo:'Josefin Sans';", content)
content = re.sub(r'--font-logo:\s*Manrope\s*;', "--font-logo:'Josefin Sans';", content)

with open('website.css', 'w') as f:
    f.write(content)

with open('index.html', 'r') as f:
    html = f.read()
    
# Ensure Josefin Sans is in the Google Fonts link
if 'Josefin+Sans' not in html:
    html = html.replace('family=Manrope', 'family=Josefin+Sans:wght@300;400;600;700&family=Manrope')

with open('index.html', 'w') as f:
    f.write(html)
