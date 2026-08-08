import re

with open("/Users/gauravmongia/.gemini/antigravity/scratch/a-K/blog/sample-post/index.html", "r") as f:
    content = f.read()

# 1. Extract TOC
toc_match = re.search(r'(<nav class="blog-toc">.*?</nav>)', content, re.DOTALL)
toc_html = toc_match.group(1) if toc_match else ""

# 2. Extract What You'll Learn
learn_start = content.find('<!-- What You\'ll Learn Section -->')
learn_end = content.find('</div>', content.find('<ul class="blog-what-you-learn-list">')) + 6
learn_html = content[learn_start:learn_end] if learn_start != -1 else ""

# 3. Extract Hero minus TOC and What You'll Learn
hero_match = re.search(r'(<header class="blog-hero">.*?</header>)', content, re.DOTALL)
if hero_match:
    hero_html = hero_match.group(1)
    if toc_html:
        hero_html = hero_html.replace(toc_html, '')
    if learn_html:
        hero_html = hero_html.replace(learn_html, '')
else:
    hero_html = ""

# 4. Remove original Hero from content
if hero_match:
    content = content.replace(hero_match.group(1), '')

# 5. Build new structure
new_structure = f"""
        {hero_html}

        <aside class="blog-left-sidebar">
            {toc_html}
        </aside>

        <!-- Main Content Column -->
        <article class="blog-main-content" id="blog-content-body">
            {learn_html}
"""

# 6. Insert new structure
content = content.replace('<!-- Main Content Column -->\n        <article class="blog-main-content" id="blog-content-body">', new_structure)

# Clean up any leftover blank lines where TOC used to be
content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

with open("/Users/gauravmongia/.gemini/antigravity/scratch/a-K/blog/sample-post/index.html", "w") as f:
    f.write(content)

print("Rewrite complete.")
