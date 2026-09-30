with open('website.css', 'r') as f:
    lines = f.readlines()

depth = 0
for i, line in enumerate(lines):
    if i > 1350: break
    for char in line:
        if char == '{':
            depth += 1
            print(f"Open at {i+1}, depth now {depth}")
        elif char == '}':
            depth -= 1
            print(f"Close at {i+1}, depth now {depth}")
