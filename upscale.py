import sys
from PIL import Image

input_path = sys.argv[1]
output_path = sys.argv[2]
target_width = 3840
target_height = 2160

img = Image.open(input_path)
img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
img.save(output_path, "WEBP", quality=100, lossless=False)
print(f"Saved upscaled image to {output_path}")
