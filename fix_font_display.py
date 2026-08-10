import os
import re

def update_font_display(directory):
    html_files = []
    for root, dirs, files in os.walk(directory):
        # skip .git or node_modules or .agents
        if '.git' in root or 'node_modules' in root or '.agents' in root or '.gemini' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    updated_files = 0
    # Match Josefin Sans and replace swap with block
    pattern = re.compile(r"(font-family:'Josefin Sans';.*?font-display:)swap;")
    
    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = pattern.sub(r"\1block;", content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                updated_files += 1
                print(f"Updated {filepath}")
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

    print(f"\nTotal files updated: {updated_files}")

if __name__ == '__main__':
    update_font_display('.')
