import re
with open('index.html', 'r') as f:
    html = f.read()

style_blocks = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
for idx, block in enumerate(style_blocks):
    open_braces = block.count('{')
    close_braces = block.count('}')
    if open_braces != close_braces:
        print(f"Mismatch in style block {idx}: Open={open_braces}, Close={close_braces}")
