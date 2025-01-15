# What is this repo? Italian Flashcards for Anki!

This project creates flashcards for Italian learners using a visual dictionary and Ollama, designed for import into Anki. The workflow includes:

    PDF Conversion: Converts the visual dictionary (PDF not included due to copyright) into images.
    Word Descriptions: Uses Ollama to generate English meanings and descriptions for each word.
    Frequency Sorting: Sorts words by frequency using Subtlex-IT, prioritizing the most common ones.

Each flashcard includes the word, an image, and a description, helping you focus on the most frequent and useful vocabulary first.
---
## Importing CSV and Images into Anki

To successfully import the flashcards into Anki:

    Generate Images:
        The images are created during the PDF-to-picture conversion in the code (each page becomes one picture).
        Ensure all images are stored in a folder named output_images.

    Place Images in Anki Media Folder:
        Move the output_images folder to Anki's media directory:
            On Android: Place the folder inside Android/data/com.anki/collection.media.
            On Other Platforms: Locate the collection.media folder in your Anki profile directory and copy the images there.

    Import the CSV File:
        Use the Import option in Anki to import the provided CSV file.
        Ensure the CSV file references the images correctly using their filenames (e.g., output_images/image1.png).

    Verify Flashcards:
        After importing, review a few cards in Anki to confirm that the images and descriptions are properly linked.
---
# How to Build and Use a Configuration File for This Project
## Step 1: Create the Configuration File

    Name the file config.json.
    Structure the file with keys for each configurable parameter.

Example File:
```{
  "api_url": "http://localhost:11111/api/chat",
  "headers": {
    "Content-Type": "application/json"
  },
  "payload_defaults": {
    "model": "llama3.2",
    "messages": [{"role": "user", "content": ""}]
  }
}

```
---
## Step 2: Understanding the Format

    JSON Format:
        Each key represents a configuration parameter.
        Keys can hold strings, objects, or arrays depending on the requirement.

### Key Breakdown:

    api_url:
        The URL for the API endpoint.
        Replace with your server's URL if different.

    prompt_template:
        A template string with a placeholder ({word}) for dynamic input.
        This allows you to customize the prompt by replacing {word} with an actual word.

    headers:
        HTTP headers required for the API request.
        Example: Content-Type specifies the type of data being sent (JSON in this case).

    payload_defaults:
        A dictionary containing the default structure of the request payload.
        The model key specifies the model to use.
        The messages key holds the default message structure.
