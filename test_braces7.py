with open('website.css', 'r') as f:
    lines = f.readlines()

depth = 0
for i, line in enumerate(lines):
    for char in line:
        if char == '{':
            depth += 1
        elif char == '}':
            depth -= 1
    if i == 4660:
        break
    if depth > 0 and '@media' in line:
        pass
    if depth == 1 and i > 4000:
        print(f"Depth 1 at line {i+1}: {line.strip()}")
