import re
import os

def replace_colors(content):
    # CSS VARIABLES
    content = re.sub(r'--deep-navy:rgba\(24, 42, 61, 0\.84\);', '--deep-navy:rgba(13, 27, 36, 0.84);', content)
    content = re.sub(r'--deep-navy-100:#182A3D;', '--deep-navy-100:#0D1B24;', content)
    content = re.sub(r'--deep-navy-84:rgba\(24, 42, 61, 0\.84\);', '--deep-navy-84:rgba(13, 27, 36, 0.84);', content)
    content = re.sub(r'--deep-navy-50:rgba\(24, 42, 61, 0\.50\);', '--deep-navy-50:rgba(13, 27, 36, 0.50);', content)
    content = re.sub(r'--refined-brass:#8C6734;', '--refined-brass:#8B5A45;', content)
    content = re.sub(r'--highlight-gold:#684A20;', '--highlight-gold:#8B5A45;', content)
    content = re.sub(r'--step-brass:#5E4119;', '--step-brass:#8B5A45;', content)
    content = re.sub(r'--antique-brass:#8C6734;', '--antique-brass:#8B5A45;', content)
    content = re.sub(r'--warm-ivory:#FBF6F3;', '--warm-ivory:#F4F1EA;', content)
    content = re.sub(r'--white:#FFFFFF;', '--white:#FFFFFF;', content)
    content = re.sub(r'--muted-slate:#4B5563;', '--muted-slate:#536068;', content)
    content = re.sub(r'--warm-stone:#EDE8E2;', '--warm-stone:#D5D1C8;', content)
    content = re.sub(r'--divider:#DDD7CF;', '--divider:#D5D1C8;', content)
    content = re.sub(r'--dark-brass:#5E4119;', '--dark-brass:#8B5A45;', content)
    content = re.sub(r'--deep-slate:#374151;', '--deep-slate:#536068;', content)

    # HEX REPLACEMENTS (Case Insensitive)
    hex_map = {
        '#182A3D': '#0D1B24',
        '#1E2432': '#0D1B24',
        '#1F2937': '#0D1B24',
        '#374151': '#536068',
        '#4B5563': '#536068',
        '#8C6734': '#8B5A45',
        '#684A20': '#8B5A45',
        '#5E4119': '#8B5A45',
        '#92400E': '#8B5A45',
        '#B88E52': '#8B5A45',
        '#C29555': '#8B5A45',
        '#FBF6F3': '#F4F1EA',
        '#FAF6F3': '#F4F1EA',
        '#FFFDF7': '#FFFFFF',
        '#FFFDF9': '#FFFFFF',
        '#F4EFE6': '#F4F1EA',
        '#F7F2EE': '#F4F1EA',
        '#EDE8E2': '#D5D1C8',
        '#E9E2D7': '#D5D1C8',
        '#E8DDD2': '#D5D1C8',
        '#DDD7CF': '#D5D1C8'
    }
    for old_hex, new_hex in hex_map.items():
        content = re.sub(old_hex, new_hex, content, flags=re.IGNORECASE)

    # RGB/RGBA REPLACEMENTS
    content = re.sub(r'24,\s*42,\s*61', '13, 27, 36', content)
    content = re.sub(r'30,\s*36,\s*50', '13, 27, 36', content)
    content = re.sub(r'33,\s*44,\s*58', '13, 27, 36', content)
    content = re.sub(r'184,\s*142,\s*82', '139, 90, 69', content)
    content = re.sub(r'251,\s*246,\s*243', '244, 241, 234', content)
    content = re.sub(r'183,\s*175,\s*164', '213, 209, 200', content)
    content = re.sub(r'233,\s*226,\s*215', '213, 209, 200', content)

    # Adjust gradient transparencies 
    content = re.sub(r'rgba\(139,\s*90,\s*69,\s*0\.14\)', 'rgba(139, 90, 69, 0.08)', content)
    content = re.sub(r'rgba\(139,\s*90,\s*69,\s*0\.08\)', 'rgba(139, 90, 69, 0.05)', content)
    content = re.sub(r'rgba\(139,\s*90,\s*69,\s*0\.07\)', 'rgba(139, 90, 69, 0.04)', content)

    return content

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for file in files:
        if file.endswith('.css') or file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            new_content = replace_colors(content)
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
