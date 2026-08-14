import os, re

new_favicon_setup = """<link rel="icon" type="image/svg+xml" href="/style-guide/assets/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/style-guide/assets/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/style-guide/assets/favicon-16x16.png">
<link rel="shortcut icon" href="/favicon.ico">
<link rel="apple-touch-icon" sizes="180x180" href="/style-guide/assets/apple-touch-icon.png">"""

for root, dirs, files in os.walk("."):
    if ".git" in root: continue
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Remove old favicon and apple-touch-icon links
            content = re.sub(r'<link[^>]*rel=["\']icon["\'][^>]*>', '', content)
            content = re.sub(r'<link[^>]*rel=["\']apple-touch-icon["\'][^>]*>', '', content)
            content = re.sub(r'<link[^>]*rel=["\']shortcut icon["\'][^>]*>', '', content)
            
            # Remove any trailing blank lines left in head (rudimentary cleanup)
            content = re.sub(r'\n\s*\n\s*</head>', '\n</head>', content)
            
            # Decide where to inject. Usually before </head>
            if "</head>" in content:
                # But wait, what if the paths need to be relative to the file?
                # The user specifically requested root-relative paths like href="/style-guide/assets/..."
                # Wait, for calculators/..., it's better to use root-relative paths like the user suggested!
                # E.g. href="/style-guide/assets/..."
                
                content = content.replace("</head>", f"{new_favicon_setup}\n</head>")
                
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Updated {path}")
