import os
import re

mapping = {
    # Greys to Muted Slate
    '#3d464e': '#55555A',
    '#55606E': '#55555A',
    '#4b5563': '#55555A',
    '#556977': '#55555A',
    '#33414C': '#55555A',
    
    # Dark to Obsidian Black
    '#2B2B2B': '#1C1C1E',
    '#0f161c': '#1C1C1E',
    
    # Oranges/Golds to Peach/Copper
    '#d8a878': '#e5b899',
    '#FFC4A3': '#e5b899',
    '#9B6248': '#804526',
    '#c57e5e': '#be7555',
    '#c47c5d': '#be7555',
    '#a85a3a': '#9f5334',
    '#a55a3a': '#9f5334',
    
    # Off-whites to Titanium Frost
    '#EAE6DF': '#FAFAFA',
    '#FAF9F6': '#FAFAFA',
    '#F7F1EA': '#FAFAFA',
    '#fbf9f5': '#FAFAFA'
}

def replace_colors(content):
    # Case insensitive replacement
    for rogue, official in mapping.items():
        content = re.sub(rogue, official, content, flags=re.IGNORECASE)
    return content

files = ['website.css', 'website.min.css', 'index.html']
for root, dirs, f_list in os.walk('.'):
    if 'landing' in root or '.agents' in root:
        continue
    for f in f_list:
        if f.endswith('.css') or f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r') as file:
                content = file.read()
            
            new_content = replace_colors(content)
            
            if new_content != content:
                with open(path, 'w') as file:
                    file.write(new_content)
                print(f"Patched {path}")

