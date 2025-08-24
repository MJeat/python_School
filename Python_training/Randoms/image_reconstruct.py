from PIL import Image
import os
import re

# Step 1: Read and parse the original_indices.txt. Don't forget to change the file name according to your saved file
with open("original_indices.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]

image_map = []

i = 0
while i < len(lines) - 1:
    if lines[i].startswith("======== ") and lines[i + 1].isdigit():
        filename = lines[i].replace("======== ", "").strip()
        
        # Skip if it's the reconstructed output file
        if filename == "reconstructed_output.png":
            i += 2
            continue
        
        index = int(lines[i + 1])
        image_map.append((index, filename))
        i += 2
    else:
        i += 1

# Step 2: Sort the list by the original index
image_map.sort()

# Step 3: Define tile and canvas size
tile_width = 48
tile_height = 13
tiles_per_row = 128 # If the image is blurry or you can't read, just adjust this to 256, 128, 64, 32, etc...
rows = (len(image_map) + tiles_per_row - 1) // tiles_per_row

# Step 4: Create a blank image canvas
final_image = Image.new("RGB", (tile_width * tiles_per_row, tile_height * rows))

# Step 5: Paste the tiles onto the canvas
for i, (index, filename) in enumerate(image_map):
    x = (i % tiles_per_row) * tile_width
    y = (i // tiles_per_row) * tile_height
    try:
        tile = Image.open(filename)
        final_image.paste(tile, (x, y))
    except Exception as e:
        print(f"⚠️ Error with {filename}: {e}")

# Step 6: Save final output
final_image.save("reconstructed_output.png")
print("✅ Successfully saved reconstructed_output.png")
