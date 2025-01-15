import fitz  # PyMuPDF
import os
import argparse

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a PDF to JPG images.")
    parser.add_argument("pdf_path", type=str, help="Path to the input PDF file.")
    parser.add_argument("output_folder", type=str, help="Path to the output folder.")
    parser.add_argument("--dpi", type=int, default=300, help="DPI for the output images (default: 300).")
    args = parser.parse_args()

    # Create the output folder if it doesn't exist
    os.makedirs(args.output_folder, exist_ok=True)

    # Convert PDF to JPG
    pdf_to_jpg_without_poppler(args.pdf_path, args.output_folder, args.dpi)