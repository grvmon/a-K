import re

def minify(filepath, outpath):
    with open(filepath, 'r') as f:
        content = f.read()
    # Remove comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    # Remove newlines and multiple spaces
    content = re.sub(r'\s+', ' ', content)
    # Remove spaces around tokens
    content = re.sub(r'\s*([\{\}\:\;\,\>])\s*', r'\1', content)
    # Remove trailing semicolons inside blocks
    content = re.sub(r';}', '}', content)
    
    with open(outpath, 'w') as f:
        f.write(content)

minify('website.css', 'website.min.css')
