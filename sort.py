import sys

# Ensure the file path and output file path are passed via the command line
if len(sys.argv) < 3:
    print("Usage: python script_name.py <input_file_path> <output_file_path>")
    sys.exit(1)

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

# Load and process the data
words = []
try:
    with open(input_file_path, 'r') as file:
        for line in file:
            word, page = line.rsplit(': ', 1)
            words.append((word.strip(), int(page.strip())))
except FileNotFoundError:
    print(f"Error: File '{input_file_path}' not found.")
    sys.exit(1)
except ValueError:
    print("Error: File content is not in the expected format ('word: page').")
    sys.exit(1)

# Sort words based on page numbers
sorted_words = sorted(words, key=lambda x: x[1])

# Save the sorted words to the specified output file
try:
    with open(output_file_path, 'w') as output_file:
        for word, page in sorted_words:
            output_file.write(f"{word}: {page}\n")
    print(f"Sorted words have been written to '{output_file_path}'.")
except Exception as e:
    print(f"Error writing to file '{output_file_path}': {e}")
    sys.exit(1)
