import os

files_to_update = [
    'header_temp.html',
    'blog/sample-post/index.html',
    'property/sumadhura-solace-whitefield/index.html'
]

replacements = {
    '#B88E52': '#9A7B4F',
    '#b88e52': '#9a7b4f',
    '#1F2B38': '#182A3D',
    '#1f2b38': '#182a3d',
    '#F7F3EC': '#FBF6F3',
    '#f7f3ec': '#fbf6f3',
    '#59616B': '#6B7280',
    '#59616b': '#6b7280',
    '#E5DED4': '#EDE8E2',
    '#e5ded4': '#ede8e2',
    '184, 142, 82': '154, 123, 79',
    '184,142,82': '154,123,79',
    '31, 43, 56': '24, 42, 61',
    '31,43,56': '24,42,61'
}

for filepath in files_to_update:
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()
        
        for old_str, new_str in replacements.items():
            content = content.replace(old_str, new_str)
            
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"File {filepath} not found.")
