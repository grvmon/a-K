import re

with open('website.css', 'r') as f:
    css = f.read()

# Remove the gradient styles for the scrolled primary cta
css = re.sub(r'\.header-nav\.scrolled \.primary-cta-btn\s*\{[^}]*\}\s*', '', css)
css = re.sub(r'\.header-nav\.scrolled \.primary-cta-btn:hover\s*\{[^}]*\}\s*', '', css)
css = re.sub(r'\.header-nav\.scrolled \.primary-cta-btn span\s*\{[^}]*\}\s*', '', css)

# Make sure the non-scrolled transparent style also applies to the scrolled header
css = css.replace(
    '.header-nav.transparent-header:not(.scrolled) .nav-cta-btn {',
    '.header-nav.transparent-header:not(.scrolled) .nav-cta-btn,\n.header-nav.scrolled .nav-cta-btn {'
)

css = css.replace(
    '.header-nav.transparent-header:not(.scrolled) .nav-cta-btn:hover {',
    '.header-nav.transparent-header:not(.scrolled) .nav-cta-btn:hover,\n.header-nav.scrolled .nav-cta-btn:hover {'
)

with open('website.css', 'w') as f:
    f.write(css)
