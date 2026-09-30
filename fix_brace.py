import re

with open('website.css', 'r') as f:
    css = f.read()

# The missing brace is right before .testimonial-card { but AFTER the cookie media query.
# Let's just find:
# .cookie-btn { ... }
# .testimonial-card {
# and insert }
css = re.sub(r'(\.cookie-btn-decline\s*\{[^}]*?\})\s*\.testimonial-card\s*\{', r'\1\n}\n\n.testimonial-card {', css)

# Wait, let's verify what the last rule is.
