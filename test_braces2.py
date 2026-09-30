with open('website.css', 'r') as f:
    lines = f.readlines()

depth = 0
for i, line in enumerate(lines):
    if i > 1350: break
    for char in line:
        if char == '{':
            depth += 1
        elif char == '}':
            depth -= 1
            if depth < 0:
                print(f"Unmatched closing brace at line {i+1}: {line.strip()}")
                depth = 0
print(f"Depth at line 1350: {depth}")
