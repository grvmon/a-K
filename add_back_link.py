import re

with open('style-guide/meta-posts-4-5.html', 'r') as f:
    html = f.read()

back_link = """
    <a href="index.html" style="position: absolute; top: 2rem; left: 2rem; color: var(--neutral-grey); text-decoration: none; font-size: 0.9rem; font-weight: 500; display: flex; align-items: center; gap: 0.5rem; transition: color 0.3s ease;">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
        Back to Styleguide
    </a>
"""

if "Back to Styleguide" not in html:
    html = html.replace('<body>', '<body>\n' + back_link)

with open('style-guide/meta-posts-4-5.html', 'w') as f:
    f.write(html)
