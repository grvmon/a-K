import re

allowed_hex = {'#be7555', '#9f5334', '#804526', '#e5b899', '#fafafa', '#1c1c1e', '#55555a', '#ffffff', '#000000'}

with open('website.css', 'r') as f:
    css = f.read()

hexes = set(re.findall(r'#[0-9a-fA-F]{3,6}', css))
rogue = [h for h in hexes if h.lower() not in allowed_hex]
if '#fff' in [r.lower() for r in rogue]:
    rogue = [r for r in rogue if r.lower() != '#fff']

print("Rogue:", len(rogue))
