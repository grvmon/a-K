import os
import re

exclude_dirs = ['archive', 'ackey-reference', 'meta-ad', '.git']
modified_count = 0

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Use regex to find "Karnataka RERA Registration No.:[space]PRM..." and replace with "<br>"
            content = re.sub(
                r"Karnataka RERA Registration No.:\s+PRM/KA/RERA/1251/446/AG/260814/007659",
                r"Karnataka RERA Registration No.:<br>PRM/KA/RERA/1251/446/AG/260814/007659",
                content
            )
            
            if content != original_content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified_count += 1
                print(f"Updated {path}")

print(f"Total modified: {modified_count}")
