import requests
import json
from tqdm import tqdm

# Function to query Ollama API
def query_ollama(word):
    api_url = "http://localhost:11434/api/chat"  # Replace with your local Ollama API endpoint if different
    prompt = f"Provide a one-line very short, concise English description for the Italian word '{word}'. Focus on meaning or common usage."
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "llama3.2",  # Replace with your model name if required
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        # Stream response
        response = requests.post(api_url, json=payload, headers=headers, stream=True)
        response.raise_for_status()

        # Collect the content from streamed chunks
        full_content = ""
        for line in response.iter_lines():
            if line:
                try:
                    chunk = line.decode("utf-8")
                    chunk_data = json.loads(chunk)  # Properly parse JSON chunk
                    if "message" in chunk_data and "content" in chunk_data["message"]:
                        full_content += chunk_data["message"]["content"]
                except json.JSONDecodeError as e:
                    print(f"Error parsing chunk: {chunk}, Error: {e}")

        return full_content.strip()
    except requests.exceptions.RequestException as e:
        print(f"HTTP error querying Ollama for '{word}': {e}")
    return None

# Read the words file
words_file = "sorted_words.txt"
output_file = "word_descriptions.txt"

descriptions = []
try:
    with open(words_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
        
        # Use tqdm to wrap the loop
        for line in tqdm(lines, desc="Processing words"):
            word, page_number = line.rsplit(":", 1)  # Split into word and page number
            word = word.strip()
            page_number = page_number.strip()
            description = query_ollama(word)
            if description:
                # Format: word: description: page_number
                descriptions.append(f"{word} @@@ {description} @@@ {page_number}")

    # Write the descriptions to a file
    with open(output_file, "w", encoding="utf-8") as out_file:
        for desc in descriptions:
            out_file.write(desc + "\n")

    print(f"Descriptions saved to {output_file}.")
except FileNotFoundError:
    print(f"File '{words_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
