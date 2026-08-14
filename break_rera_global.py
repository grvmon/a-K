import os

exclude_dirs = ['archive', 'ackey-reference', 'meta-ad', '.git']
modified_count = 0

old_str = "Karnataka RERA Registration No.: PRM/KA/RERA/1251/446/AG/260814/007659"
new_str = "Karnataka RERA Registration No.:<br>PRM/KA/RERA/1251/446/AG/260814/007659"

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            if old_str in content:
                content = content.replace(old_str, new_str)
            
            if content != original_content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified_count += 1
                print(f"Updated {path}")

print(f"Total modified: {modified_count}")
