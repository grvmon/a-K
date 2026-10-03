with open('index.html', 'r') as f:
    html = f.read()
import re
styles = re.findall(r'<style>(.*?)</style>', html, flags=re.DOTALL)
if styles:
    for block in styles[0].split('}'):
        if 'transition: all' in block:
            print(block.strip() + '}')
