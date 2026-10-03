import re

with open('website.css', 'r') as f:
    css = f.read()

# Extract hex colors
hex_colors = set(re.findall(r'#[0-9a-fA-F]{3,6}', css))
print("Hex colors in website.css:")
print(hex_colors)

# Extract rgba colors
rgba_colors = set(re.findall(r'rgba\([^)]+\)', css))
print("RGBA colors in website.css:")
print(rgba_colors)

