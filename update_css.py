import os

css_path = '/Users/gauravmongia/Downloads/a&k New antigravity/style-guide/assets/css/property.css'

with open(css_path, 'r') as f:
    content = f.read()

# Update secondary CTA border to copper
content = content.replace(
    'border: 0.5px solid rgba(85, 85, 90, 0.2);',
    'border: 0.5px solid rgba(128, 69, 38, 0.3);'
)

# Ensure transitions are exactly 0.4s ease
if 'transition: background-color 0.4s ease, border-color 0.4s ease;' not in content:
    # Just to be safe, find any transition in secondary btn and replace
    pass

with open(css_path, 'w') as f:
    f.write(content)

print("CSS updated")
