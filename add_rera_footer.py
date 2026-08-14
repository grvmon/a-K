import os

exclude_dirs = ['archive', 'ackey-reference', 'meta-ad', '.git']
target_phrase = "Karnataka 560087</span>"
replacement_phrase = "Karnataka 560087<br><br>Karnataka RERA Registration No.: PRM/KA/RERA/1251/446/AG/260814/007659</span>"
modified_count = 0

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if target_phrase in content and "PRM/KA/RERA/1251/446/AG/260814/007659" not in content:
                content = content.replace(target_phrase, replacement_phrase)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified_count += 1
                print(f"Updated {path}")

print(f"Total modified: {modified_count}")
