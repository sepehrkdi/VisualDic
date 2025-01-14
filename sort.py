# Let's parse the provided text file and sort the words based on their page numbers.
file_path = 'words.txt'

# Load and process the data
words = []
with open(file_path, 'r') as file:
    for line in file:
        word, page = line.rsplit(': ', 1)
        words.append((word.strip(), int(page.strip())))

# Sort words based on page numbers
sorted_words = sorted(words, key=lambda x: x[1])

# Define the output file path
output_file_path = 'sorted_words.txt'

# Save the sorted words to a new text file
with open(output_file_path, 'w') as output_file:
    for word, page in sorted_words:
        output_file.write(f"{word}: {page}\n")