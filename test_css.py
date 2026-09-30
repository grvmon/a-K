import re
with open('website.css', 'r') as f:
    css = f.read()

# Let's count { and }
open_braces = css.count('{')
close_braces = css.count('}')
print(f"Open: {open_braces}, Close: {close_braces}")
