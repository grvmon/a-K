import os
import re

dir_path = "/Users/gauravmongia/.gemini/antigravity/scratch/a-K"

for filename in ["index.html", "website.js", "website.css"]:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, "r") as f:
        content = f.read()
    
    # Replace v=17 with v=18
    new_content = re.sub(r'v=17', 'v=18', content)
    
    if new_content != content:
        with open(filepath, "w") as f:
            f.write(new_content)
        print(f"Updated {filename}")
