import os
import json

# Define supported image extensions
image_extensions = {".png", ".jpg", ".jpeg", ".webp"}

# Get all image files in the current directory and sort them lexically
image_files = sorted([f for f in os.listdir('.') if os.path.splitext(f)[1].lower() in image_extensions])

# Generate JSON data with indexed images
image_data = [{"id": i, "name": image} for i, image in enumerate(image_files)]

# Save to a JSON file
json_filename = "images.json"
with open(json_filename, "w", encoding="utf-8") as f:
    json.dump(image_data, f, indent=4)

# Output the JSON content as well for reference
json.dumps(image_data, indent=4)
