import os
import re
import urllib.request
import urllib.parse
from pathlib import Path

urls = [
    "https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@300;400;500;600;700&family=Manrope:wght@300;400;500;600;700;800&family=Marcellus&display=swap",
    "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

fonts_dir = Path("/Users/gauravmongia/.gemini/antigravity/scratch/a-K/style-guide/assets/fonts")
fonts_dir.mkdir(parents=True, exist_ok=True)

css_output_path = Path("/Users/gauravmongia/.gemini/antigravity/scratch/a-K/fonts.css")

final_css = ""

import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for url in urls:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx) as response:
        css_content = response.read().decode('utf-8')
    
    def replacer(match):
        font_url = match.group(1)
        filename = font_url.split('/')[-1]
        local_path = fonts_dir / filename
        
        if not local_path.exists():
            print(f"Downloading {filename}...")
            font_req = urllib.request.Request(font_url, headers=headers)
            with urllib.request.urlopen(font_req, context=ctx) as font_response:
                local_path.write_bytes(font_response.read())
        
        return f"url('style-guide/assets/fonts/{filename}')"

    modified_css = re.sub(r'url\((https://[^)]+)\)', replacer, css_content)
    final_css += modified_css + "\n\n"

css_output_path.write_text(final_css)
print("Finished downloading fonts and creating fonts.css")
