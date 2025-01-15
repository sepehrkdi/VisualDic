import csv
import os
import sys

# Ensure the correct number of arguments are provided
if len(sys.argv) != 4:
    print("Usage: python script.py <media_folder> <word_descriptions_file> <output_file>")
    sys.exit(1)

# Read arguments from the command line
media_folder = sys.argv[1]
word_descriptions_file = sys.argv[2]
output_file = sys.argv[3]

# Process the word descriptions file
try:
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
        with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter="\t")  # Use tab as delimiter
            writer.writerows(rows)

        print(f"Anki deck with images saved as {output_file}.")

except FileNotFoundError:
    print(f"Error: File '{word_descriptions_file}' not found.")
    sys.exit(1)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)
