import os
import re

exclude_dirs = ['archive', 'ackey-reference', 'meta-ad', '.git']

old_footer = """<footer class=site-footer id=footer><div class=container><div class=footer-bottom-bar style="border-top: none; padding-top: 10px;"><div class=footer-bottom-left><span>© 2026 Acrenkey Realty LLP. All rights reserved.</span><span style="display:block; margin-top: 6px; color: rgba(255, 255, 255, 0.45); font-size: 0.85em; line-height: 1.5; max-width: 340px;">Innov8 Prestige Tech Platina, 11th Floor, No. 32/2, 34/1, Kadubeesanahalli, Marathahalli, Bengaluru, Karnataka 560087<br><br>Karnataka RERA Registration No.: PRM/KA/RERA/1251/446/AG/260814/007659</span></div><div class=footer-social-icons style="margin-top: 0;"><a href="https://www.facebook.com/profile.php?id=61589792184848" target=_blank rel="noopener noreferrer" aria-label=Facebook><i class="fa-brands fa-facebook-f"></i></a><a href=https://www.instagram.com/acrenkey/ target=_blank rel="noopener noreferrer" aria-label=Instagram><i class="fa-brands fa-instagram"></i></a><a href=https://www.youtube.com/channel/UC-6WtLxFOaR_X2y7FQTBcHw target=_blank rel="noopener noreferrer" aria-label=YouTube><i class="fa-brands fa-youtube"></i></a><a href=https://x.com/acreNkey target=_blank rel="noopener noreferrer" aria-label=Twitter><i class="fa-brands fa-twitter"></i></a><a href=https://www.linkedin.com/company/acrenkey/ target=_blank rel="noopener noreferrer" aria-label=LinkedIn><i class="fa-brands fa-linkedin-in"></i></a><a href=https://www.reddit.com/user/acreNkey/ target=_blank rel="noopener noreferrer" aria-label=Reddit><i class="fa-brands fa-reddit-alien"></i></a><a href=https://www.quora.com/profile/AcreNkey target=_blank rel="noopener noreferrer" aria-label=Quora><i class="fa-brands fa-quora"></i></a><a href=https://pin.it/58qQo3rsD target=_blank rel="noopener noreferrer" aria-label=Pinterest><i class="fa-brands fa-pinterest-p"></i></a></div><div class=footer-bottom-right><ul class=footer-legal-links><li><a href=/careers>Careers</a></li><li><a href=/privacy-policy/ >Privacy Policy</a></li><li><a href=/terms-of-service/ >Terms of Service</a></li><li><a href=/rera-disclaimer/ >RERA Disclaimer</a></li></ul></div></div></div></footer>"""

new_footer = """<footer class=site-footer id=footer><div class=container><div class=footer-bottom-bar style="border-top: none; padding-top: 10px;"><div class=footer-bottom-left><span>© 2026 Acrenkey Realty LLP. All rights reserved.</span><span style="display:block; margin-top: 6px; color: rgba(255, 255, 255, 0.45); font-size: 0.85em; line-height: 1.5; max-width: 340px;">Innov8 Prestige Tech Platina, 11th Floor, No. 32/2, 34/1, Kadubeesanahalli, Marathahalli, Bengaluru, Karnataka 560087</span></div><div class=footer-social-icons style="margin-top: 0;"><a href="https://www.facebook.com/profile.php?id=61589792184848" target=_blank rel="noopener noreferrer" aria-label=Facebook><i class="fa-brands fa-facebook-f"></i></a><a href=https://www.instagram.com/acrenkey/ target=_blank rel="noopener noreferrer" aria-label=Instagram><i class="fa-brands fa-instagram"></i></a><a href=https://www.youtube.com/channel/UC-6WtLxFOaR_X2y7FQTBcHw target=_blank rel="noopener noreferrer" aria-label=YouTube><i class="fa-brands fa-youtube"></i></a><a href=https://x.com/acreNkey target=_blank rel="noopener noreferrer" aria-label=Twitter><i class="fa-brands fa-twitter"></i></a><a href=https://www.linkedin.com/company/acrenkey/ target=_blank rel="noopener noreferrer" aria-label=LinkedIn><i class="fa-brands fa-linkedin-in"></i></a><a href=https://www.reddit.com/user/acreNkey/ target=_blank rel="noopener noreferrer" aria-label=Reddit><i class="fa-brands fa-reddit-alien"></i></a><a href=https://www.quora.com/profile/AcreNkey target=_blank rel="noopener noreferrer" aria-label=Quora><i class="fa-brands fa-quora"></i></a><a href=https://pin.it/58qQo3rsD target=_blank rel="noopener noreferrer" aria-label=Pinterest><i class="fa-brands fa-pinterest-p"></i></a></div><div class=footer-bottom-right style="display: flex; flex-direction: column; align-items: flex-end; gap: 8px;"><span style="color: rgba(255, 255, 255, 0.45); font-size: 0.85em;">Karnataka RERA Registration No.: PRM/KA/RERA/1251/446/AG/260814/007659</span><ul class=footer-legal-links style="margin:0;"><li><a href=/careers>Careers</a></li><li><a href=/privacy-policy/ >Privacy Policy</a></li><li><a href=/terms-of-service/ >Terms of Service</a></li><li><a href=/rera-disclaimer/ >RERA Disclaimer</a></li></ul></div></div></div></footer>"""

modified_count = 0

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if old_footer in content:
                content = content.replace(old_footer, new_footer)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified_count += 1
                print(f"Updated {path}")

print(f"Total modified: {modified_count}")
