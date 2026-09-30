with open('website.css', 'r') as f:
    lines = f.readlines()

depth = 0
for i, line in enumerate(lines):
    if i > 2000: break
    for char in line:
        if char == '{':
            depth += 1
            if depth == 1: print(f"Depth 1 -> 2 at {i+1}")
        elif char == '}':
            depth -= 1
            if depth == 0: print(f"Depth 1 -> 0 at {i+1}")
