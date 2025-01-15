#!/bin/bash

source venv/bin/activate

PDF_PATH="italian_english_bilingual_visual_dic.pdf"
OUTPUT_FOLDER="output_images"
UNSORTED_FILE_PATH="words.txt"
SORTED_FILE_PATH="sorted_words.txt"
OLLAMA_OUTPUT="word_descriptions.txt"
ANKI_OUTPUT="anki_deck_with_images.csv"
SUBTLEX_FILE_PATH="subtlex-it.csv"

python3 pdfToImage.py "$PDF_PATH" "$OUTPUT_FOLDER"
python3 ollama.py "$UNSORTED_FILE_PATH" "$OLLAMA_OUTPUT"
python3 sort.py "$OLLAMA_OUTPUT" "$SORTED_FILE_PATH" "$SUBTLEX_FILE_PATH"
python3 anki.py "$OUTPUT_FOLDER" "$SORTED_FILE_PATH" "$ANKI_OUTPUT"

deactivate