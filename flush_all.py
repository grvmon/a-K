import os
import re

dir_path = "/Users/patidar/Desktop/AnK website"

html_files = []
for root, dirs, files in os.walk(dir_path):
    if '.git' in root or '.agents' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace v=NUM with v=NUM+1 for simple ones like v=56
    def bump_simple(match):
        return f"v={int(match.group(1)) + 1}"
    
    new_content = re.sub(r'v=(\d+)$', bump_simple, content)
    new_content = re.sub(r'v=(\d+)"', lambda m: f'v={int(m.group(1))+1}"', new_content)
    new_content = re.sub(r'v=(\d+)\'', lambda m: f"v={int(m.group(1))+1}'", new_content)

    # Replace the complex ones v=...flush_cache_v...
    new_content = re.sub(r'v=\d+_flush_cache_v\d+', 'v=20260812_flush_cache_v6', new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Bumped cache in {filepath}")
