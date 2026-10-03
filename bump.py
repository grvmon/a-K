import re, time
ts = str(int(time.time()))
for h in ['index.html']:
    with open(h, 'r') as f: c = f.read()
    c = re.sub(r'(\.css\?v=)[a-zA-Z0-9_]+', r'\g<1>' + ts, c)
    c = re.sub(r'(\.js\?v=)[a-zA-Z0-9_]+', r'\g<1>' + ts, c)
    with open(h, 'w') as f: f.write(c)
