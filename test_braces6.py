with open('website.css', 'r') as f:
    lines = f.readlines()

depth = 0
for i, line in enumerate(lines):
    if '@media' in line:
        print(f"Media query starts at line {i+1}: {line.strip()}")
    for char in line:
        if char == '{':
            depth += 1
        elif char == '}':
            depth -= 1
            if depth == 0 and '@media' not in line:
                pass
    if i == 4660:
        print(f"Depth at line 4660: {depth}")
