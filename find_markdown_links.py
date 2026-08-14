import os, re
found = False
for root, dirs, files in os.walk("."):
    if ".git" in root: continue
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            # search for [...](...) in hrefs or src
            matches = re.findall(r"(href|src)=[\"']\[(.*?)\]\((.*?)\)[\"']", content)
            if matches:
                found = True
                print(f"FOUND IN {path}:")
                for m in matches:
                    print(f"  {m[0]}=[{m[1]}]({m[2]})")
if not found:
    print("NO MARKDOWN LINKS FOUND IN ATTRIBUTES")
