import os

exclude_dirs = ['archive', 'ackey-reference', 'meta-ad', '.git']
target_phrase = '<div class="footer-bottom-left">&copy; 2026 acreNkey. All rights reserved.</div>'

replacement_phrase = """<div class="footer-bottom-left">
<span>© 2026 Acrenkey Realty LLP. All rights reserved.</span>
<span style="display:block; margin-top: 6px; color: rgba(255, 255, 255, 0.45); font-size: 0.85em; line-height: 1.5; max-width: 340px;">Innov8 Prestige Tech Platina, 11th Floor, No. 32/2, 34/1, Kadubeesanahalli, Marathahalli, Bengaluru, Karnataka 560087<br><br>Karnataka RERA Registration No.: PRM/KA/RERA/1251/446/AG/260814/007659</span>
</div>"""

modified_count = 0

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if target_phrase in content:
                content = content.replace(target_phrase, replacement_phrase)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified_count += 1
                print(f"Updated {path}")

print(f"Total modified: {modified_count}")
