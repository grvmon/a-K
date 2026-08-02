import os
from PIL import Image

assets_dir = 'style-guide/assets'

# Target widths for images used on the site
target_widths = {
    'acrekey_bengaluru_hero_advisor.jpg': 1200,
    'acrekey_construction_vs_ready.jpg': 800,
    'Rajveer Meena.png': 150,
    'Nitin Kocchar.png': 150,
    'arun goyal.jpeg': 150,
    'nitin_gupta.jpg': 256,
    'arvind_patidar.jpg': 256,
    'favicon.jpg': 48,
    'bengaluru_couple_tablet.jpg': 800,
    'bengaluru_family_balcony.jpg': 800,
    'bengaluru_micromarket_map.jpg': 1000,
    'clarity_buyer_advisor.jpg': 800,
    'clarity_couple_alone.jpg': 800,
    'family_balcony.jpg': 800,
    'hni_family_dog_balcony.jpg': 800,
    'luxury_keys.jpg': 600,
    'minimal_living_room.jpg': 600,
    'modern_staircase.jpg': 600,
    'news_diligence_buying.jpg': 600,
    'news_east_bangalore.jpg': 600,
    'news_premium_housing.jpg': 600,
    'stressed_buyer_couple.jpg': 800,
    'test.jpg': 600
}

# Keep track of renamed paths to rewrite HTML/CSS
replacements = {}

for filename in os.listdir(assets_dir):
    filepath = os.path.join(assets_dir, filename)
    if not os.path.isfile(filepath):
        continue
        
    ext = os.path.splitext(filename)[1].lower()
    if ext not in ['.jpg', '.jpeg', '.png']:
        continue
        
    print(f"Processing {filename}...")
    try:
        with Image.open(filepath) as img:
            # Determine new filename (replace spaces and change extension to .webp)
            new_base = os.path.splitext(filename)[0].replace(' ', '_')
            new_filename = f"{new_base}.webp"
            new_filepath = os.path.join(assets_dir, new_filename)
            
            # Check if there is a target width defined
            if filename in target_widths:
                width = target_widths[filename]
                if img.width > width:
                    # Calculate new height maintaining aspect ratio
                    ratio = width / float(img.width)
                    height = int(float(img.height) * float(ratio))
                    print(f"Resizing from {img.width}x{img.height} to {width}x{height}")
                    img = img.resize((width, height), Image.Resampling.LANCZOS)
            
            # Save as WebP
            img.save(new_filepath, 'WEBP', quality=82)
            print(f"Saved to {new_filepath}")
            
            # Register replacement path
            old_rel_path = f"style-guide/assets/{filename}"
            new_rel_path = f"style-guide/assets/{new_filename}"
            replacements[old_rel_path] = new_rel_path
            
            # Special check for URL encoded space in html/css
            old_encoded_path = f"style-guide/assets/{filename.replace(' ', '%20')}"
            replacements[old_encoded_path] = new_rel_path

    except Exception as e:
        print(f"Error processing {filename}: {e}")

# Now update index.html and website.css
files_to_update = ['index.html', 'website.css']

for file_to_update in files_to_update:
    if not os.path.exists(file_to_update):
        continue
    print(f"Updating references in {file_to_update}...")
    with open(file_to_update, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    for old_path, new_path in replacements.items():
        if old_path in content:
            print(f"Replacing {old_path} -> {new_path}")
            content = content.replace(old_path, new_path)
            
    if content != original_content:
        with open(file_to_update, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully updated {file_to_update}")
    else:
        print(f"No replacements needed in {file_to_update}")

print("Image optimization complete!")
