import sys
import csv

# Ensure the file path and output file path are passed via the command line
if len(sys.argv) < 4:
    print("Usage: python script_name.py <input_file_path> <output_file_path> <subtlex_file_path>")
    sys.exit(1)

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]
subtlex_file_path = sys.argv[3]

# Load word frequency data from subtlex-it.csv
word_frequency = {}
try:
    with open(subtlex_file_path, 'r', encoding='iso-8859-1') as subtlex_file:
        csv_reader = csv.DictReader(subtlex_file, delimiter=';')
        for row in csv_reader:
            word = row['wordform'].strip().lower()
            freq_value = row['freq_count'].strip()  # Frequency per million words
            if freq_value:  # Check if the frequency field is not empty
                frequency = float(freq_value.replace(',', '.'))  # Convert frequency to float
                word_frequency[word] = frequency
            else:
                word_frequency[word] = 0  # Default frequency for empty values
            word_frequency[word] = frequency
except FileNotFoundError:
    print(f"Error: File '{subtlex_file_path}' not found.")
    sys.exit(1)
except KeyError:
    print("Error: 'subtlex-it.csv' is missing required columns.")

    sys.exit(1)

# Load and process the input file
data = []
try:
    with open(input_file_path, 'r') as file:
        for line in file:
            try:
                word, des, page = line.split('@@@')
                word = word.strip().lower()
                page = int(page.strip())
                frequency = word_frequency.get(word, 0)  # Default frequency is 0 if not found
                data.append((word, des, page, frequency))
            except ValueError:
                continue
                # print("Error: File content is not in the expected format ('word: page').")
                # sys.exit(1)
except FileNotFoundError:
    print(f"Error: File '{input_file_path}' not found.")
    sys.exit(1)

# Sort words based on frequency (descending order)
data.sort(key=lambda x: (-x[3], x[0]))

# Save the sorted words to the specified output file
try:
    with open(output_file_path, 'w') as output_file:
        for word, des, page, frequency in data:
            output_file.write(f"{word} @@@ {des} @@@ {page}\n")
    print(f"Sorted words have been written to '{output_file_path}'.")
except Exception as e:
    print(f"Error writing to file '{output_file_path}': {e}")
    sys.exit(1)
