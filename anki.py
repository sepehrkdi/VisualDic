import csv
import os

# Media folder where images are stored
media_folder = "output_images"
word_descriptions_file = "word_descriptions.txt"

with open(word_descriptions_file, "r", encoding="utf-8") as file:
    lines = file.readlines()
    # Parse the text and generate Anki-compatible data
    rows = []
    for line in lines:
        parts = line.split("@@@")
        if len(parts) == 3:
            front = parts[0].strip()
            back_description = parts[1].strip()
            page = str(int(parts[2].strip()) + 2)  # Adjust page number
            image_file = f"page_{page}.jpg"
            image_path = os.path.join(media_folder, image_file)
        if os.path.exists(image_path):
            back = f"{back_description}<br><img src=\"{image_path}\">"
        else:
            back = f"{back_description}<br>[Image missing for page {page}]"
        rows.append([front, back])

# Output to a CSV file
output_file = "anki_deck_with_images.csv"
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter="\t")  # Use tab as delimiter
    writer.writerows(rows)

print(f"Anki deck with images saved as {output_file}.")