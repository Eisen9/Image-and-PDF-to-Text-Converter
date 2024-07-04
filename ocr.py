import os
import argparse
from PIL import Image
import pytesseract
import io
import sys
import subprocess
import importlib

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def safe_import(package):
    try:
        return importlib.import_module(package)
    except ImportError:
        print(f"Attempting to install {package}...")
        install_package(package)
        return importlib.import_module(package)

# Safely import or install necessary packages
pdf2image = safe_import('pdf2image')
PyPDF2 = safe_import('PyPDF2')

def convert_image_to_text(image):
    try:
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return f"Error processing image: {str(e)}"

def convert_pdf_to_text_ocr(pdf_path):
    try:
        pages = pdf2image.convert_from_path(pdf_path)
        text = ""
        for page in pages:
            img_byte_arr = io.BytesIO()
            page.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            text += pytesseract.image_to_string(Image.open(io.BytesIO(img_byte_arr))) + "\n\n"
        return text
    except Exception as e:
        return f"Error processing PDF with OCR: {str(e)}"

def convert_pdf_to_text_pypdf2(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n\n"
        return text
    except Exception as e:
        return f"Error processing PDF with PyPDF2: {str(e)}"

def process_file_or_directory(path):
    results = {}
    
    if os.path.isfile(path):
        if path.lower().endswith('.pdf'):
            text = convert_pdf_to_text_ocr(path)
            if "Error processing PDF with OCR" in text:
                text = convert_pdf_to_text_pypdf2(path)
        else:
            with Image.open(path) as img:
                text = convert_image_to_text(img)
        results[os.path.basename(path)] = text
    elif os.path.isdir(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', '.pdf')):
                results[filename] = process_file_or_directory(file_path)[os.path.basename(file_path)]
    else:
        print(f"Error: {path} is not a valid file or directory")
    
    return results

def main():
    parser = argparse.ArgumentParser(description="Convert images and PDFs to text using OCR and other methods")
    parser.add_argument("path", help="Path to an image file, PDF, or directory containing images/PDFs")
    parser.add_argument("-o", "--output", help="Output file to save the results (optional)")
    args = parser.parse_args()

    results = process_file_or_directory(args.path)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            for filename, text in results.items():
                f.write(f"--- {filename} ---\n{text}\n\n")
        print(f"Results saved to {args.output}")
    else:
        for filename, text in results.items():
            print(f"--- {filename} ---")
            print(text)
            print()

if __name__ == "__main__":
    main()