import os
import re

exclude_dirs = ['archive', 'ackey-reference', 'meta-ad', '.git']
modified_count = 0

rera_text = r"<br><br>Karnataka RERA Registration No.: PRM/KA/RERA/1251/446/AG/260814/007659"
rera_injection = r'<div class="footer-bottom-right" style="display: flex; flex-direction: column; align-items: flex-end; gap: 8px;"><span style="color: rgba(255, 255, 255, 0.45); font-size: 0.85em; text-align: right;">Karnataka RERA Registration No.: PRM/KA/RERA/1251/446/AG/260814/007659</span>\n<ul class="footer-legal-links" style="margin:0;">'

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Remove RERA from the left side if it exists
            content = content.replace("<br><br>Karnataka RERA Registration No.: PRM/KA/RERA/1251/446/AG/260814/007659", "")
            
            # Inject RERA on the right side if it hasn't been injected yet
            if "flex-direction: column" not in content and "Karnataka RERA Registration No" not in content.split("footer-bottom-right")[1] if "footer-bottom-right" in content else False:
                content = re.sub(
                    r'<div class=["\']?footer-bottom-right["\']?>\s*<ul class=["\']?footer-legal-links["\']?>',
                    rera_injection,
                    content
                )
            
            if content != original_content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified_count += 1
                print(f"Updated {path}")

print(f"Total modified: {modified_count}")
