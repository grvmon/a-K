import os
import re

exclude_dirs = ['archive', 'ackey-reference', 'meta-ad', '.git']
modified_count = 0

old_rera_span = r'<span style="color: rgba(255, 255, 255, 0.45); font-size: 0.85em; text-align: right;">Karnataka RERA Registration No.: PRM/KA/RERA/1251/446/AG/260814/007659</span>'
old_rera_span_var2 = r'<span style="color: rgba(255, 255, 255, 0.45); font-size: 0.85em;">Karnataka RERA Registration No.: PRM/KA/RERA/1251/446/AG/260814/007659</span>'

new_rera_span = r'<span style="color: rgba(255, 255, 255, 0.45); font-size: 0.85em; text-align: right;">Karnataka RERA Registration No.:<br>PRM/KA/RERA/1251/446/AG/260814/007659</span>'

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            if old_rera_span in content:
                content = content.replace(old_rera_span, new_rera_span)
            elif old_rera_span_var2 in content:
                content = content.replace(old_rera_span_var2, new_rera_span)
            
            if content != original_content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified_count += 1
                print(f"Updated {path}")

print(f"Total modified: {modified_count}")
