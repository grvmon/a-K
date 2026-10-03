from PIL import Image

# Open the image
img = Image.open('style-guide/assets/piyush-mittal-cbo-partner-acre-key.jpg')
width, height = img.size

# We want to crop out the bottom and zoom into the face.
# The finger is at the bottom.
# Let's crop the center-top portion.
# Left, Top, Right, Bottom
new_left = width * 0.15
new_top = height * 0.05
new_right = width * 0.85
new_bottom = height * 0.65

# Crop the image
cropped_img = img.crop((new_left, new_top, new_right, new_bottom))

# Save it back
cropped_img.save('style-guide/assets/piyush-mittal-cbo-partner-acre-key.jpg')
