import os
import re

exclude_dirs = ['archive', 'ackey-reference', 'meta-ad', '.git']
modified_count = 0

new_bottom_bar = """<div class="footer-bottom-bar" style="border-top: none; padding-top: 10px;">
    <div class="footer-bottom-left">
        <span>© 2026 Acrenkey Realty LLP. All rights reserved.</span>
        <span style="display:block; margin-top: 6px; color: rgba(255, 255, 255, 0.45); font-size: 0.85em; line-height: 1.5; max-width: 340px;">Innov8 Prestige Tech Platina, 11th Floor, No. 32/2, 34/1, Kadubeesanahalli, Marathahalli, Bengaluru, Karnataka 560087</span>
    </div>
    <div class="footer-bottom-right" style="display: flex; flex-direction: column; align-items: flex-end; gap: 8px;">
        <span style="color: rgba(255, 255, 255, 0.45); font-size: 0.85em; text-align: right;">Karnataka RERA Registration No.:<br>PRM/KA/RERA/1251/446/AG/260814/007659</span>
        <ul class="footer-legal-links" style="margin:0;">
            <li><a href="/careers/">Careers</a></li>
            <li><a href="/privacy-policy/">Privacy Policy</a></li>
            <li><a href="/terms-of-service/">Terms of Service</a></li>
            <li><a href="/rera-disclaimer/">RERA Disclaimer</a></li>
        </ul>
    </div>
</div>"""

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Use regex to find the old footer-bottom-bar in calculators
            match = re.search(r'<div class="footer-bottom-bar">\s*<div class="footer-bottom-left">.*?</ul>\s*</div>', content, flags=re.DOTALL)
            
            if match:
                content = content.replace(match.group(0), new_bottom_bar)
            
            if content != original_content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified_count += 1
                print(f"Updated {path}")

print(f"Total modified: {modified_count}")
