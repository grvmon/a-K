import os
import re
from xml.sax.saxutils import escape

base_url = "https://acrenkey.com"
exclude_dirs = ['archive', 'ackey-reference', 'meta-ad', '.git']
image_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.svg', '.gif')

sitemap_entries = []

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            # Create page URL
            page_path = filepath.replace('./', '').replace('index.html', '')
            if page_path == '':
                page_url = base_url + '/'
            else:
                page_url = base_url + '/' + page_path
                
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find images (<img> and <source>)
            images = []
            
            # Match <img src="X">
            img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
            # Match <source srcset="X">
            srcsets = re.findall(r'<source[^>]+srcset=["\']([^"\', ]+)["\']', content)
            # Match CSS background images in style tags or inline styles? Usually only standard img/picture tags are indexed by Google Image Search.
            # Match og:image meta tags
            og_images = re.findall(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', content)
            
            all_raw_srcs = img_srcs + srcsets + og_images
            
            # Clean and deduplicate images
            page_images = set()
            for src in all_raw_srcs:
                # Remove query params like ?v=...
                src = src.split('?')[0]
                
                # Check if it's an image
                if not src.lower().endswith(image_extensions):
                    continue
                
                # Ignore base64
                if src.startswith('data:'):
                    continue
                
                # Resolve relative paths
                if src.startswith('http'):
                    if 'acrenkey.com' in src:
                        img_url = src
                    else:
                        continue # external image
                elif src.startswith('/'):
                    img_url = base_url + src
                else:
                    # Resolve relative to the current file path
                    # E.g. filepath: ./property/sumadhura/index.html, src: ../../style-guide/assets/img.jpg
                    dir_path = os.path.dirname(filepath)
                    resolved_path = os.path.normpath(os.path.join(dir_path, src))
                    img_url = base_url + '/' + resolved_path.replace('./', '')
                
                page_images.add(img_url)
            
            if page_images:
                entry = f"  <url>\n    <loc>{escape(page_url)}</loc>\n"
                for img_url in page_images:
                    entry += f"    <image:image>\n      <image:loc>{escape(img_url)}</image:loc>\n    </image:image>\n"
                entry += "  </url>"
                sitemap_entries.append(entry)

sitemap_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
{chr(10).join(sitemap_entries)}
</urlset>'''

with open('image-sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_xml)

print(f"Generated image-sitemap.xml with {len(sitemap_entries)} pages containing images.")
