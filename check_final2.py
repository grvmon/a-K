import re
with open('index.html', 'r') as f:
    html = f.read()
styles = re.findall(r'<style>(.*?)</style>', html, flags=re.DOTALL)
if styles:
    for block in styles[0].split('}'):
        if 'font-size' in block and '14px' in block and 'subtitle' in block:
            print(block.strip() + '}')
