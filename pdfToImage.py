import fitz  # PyMuPDF
import os

def pdf_to_jpg_without_poppler(pdf_path, output_folder, dpi=300):
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    for page_number in range(len(pdf_document)):
        # Select the page
        page = pdf_document[page_number]
        # Render the page as an image
        pix = page.get_pixmap(dpi=dpi)
        # Define the output file path
        output_path = os.path.join(output_folder, f"page_{page_number + 1}.jpg")
        # Save as JPG
        pix.save(output_path)
        print(f"Saved: {output_path}")
    pdf_document.close()

# Example usage
pdf_path = "italian_english_bilingual_visual_dic.pdf"  # Replace with your PDF file path
output_folder = "output_images"    # Replace with desired output folder

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Convert PDF to JPG
pdf_to_jpg_without_poppler(pdf_path, output_folder)
