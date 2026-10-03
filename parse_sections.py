from bs4 import BeautifulSoup
import re

with open('index.html', 'r') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("--- SECTIONS ---")
sections = soup.find_all('section')
for i, s in enumerate(sections):
    id_attr = s.get('id', 'N/A')
    class_attr = ' '.join(s.get('class', []))
    print(f"Section {i+1}: ID={id_attr}, Class={class_attr}")

print("\n--- FOOTER ---")
footer = soup.find('footer')
if footer:
    print(f"Footer: ID={footer.get('id', 'N/A')}, Class={' '.join(footer.get('class', []))}")
