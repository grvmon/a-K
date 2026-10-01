import os
import re

# Rename file
old_file = 'style-guide/meta-ads-moodboard.html'
new_file = 'style-guide/meta-posts-4-5.html'

# Update HTML file
with open(old_file, 'r') as f:
    content = f.read()

content = content.replace('Ultra-HNI Visual Moodboard (3:4)', 'Meta Posts Moodboard (4:5)')

with open(new_file, 'w') as f:
    f.write(content)

os.remove(old_file)

# Update references in index.html
with open('style-guide/index.html', 'r') as f:
    index_content = f.read()

index_content = index_content.replace('meta-ads-moodboard.html', 'meta-posts-4-5.html')
index_content = index_content.replace('Meta Ads Styleguide', 'Meta Posts (4:5) Styleguide')
index_content = index_content.replace('Meta Ads', 'Meta Posts (4:5)')

with open('style-guide/index.html', 'w') as f:
    f.write(index_content)

