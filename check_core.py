from bs4 import BeautifulSoup

with open('index.html', 'r') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
core = soup.find(id='core')
if core:
    print(core.text[:500])
