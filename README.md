# Image and PDF to Text Converter

This project provides a Python script that converts images and PDF files containing text into plain text using Optical Character Recognition (OCR). It can process individual files or entire directories, supporting various image formats and PDF files.

## Features

- Convert images (PNG, JPG, JPEG, TIFF, BMP, GIF) to text
- Convert PDF files to text
- Process individual files or entire directories
- Output results to console or a specified file

## Requirements

- Python 3.6+
- Tesseract OCR
- Poppler (for PDF support)

## Installation

1. Clone this repository or download the script.

2. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

3. Install Tesseract OCR:
   - Ubuntu or Debian: `sudo apt-get install tesseract-ocr`
   - macOS with Homebrew: `brew install tesseract`
   - Windows: Download the installer from the [GitHub releases page](https://github.com/UB-Mannheim/tesseract/wiki)

4. Install Poppler:
   - Ubuntu or Debian: `sudo apt-get install poppler-utils`
   - macOS with Homebrew: `brew install poppler`
   - Windows: Download the [poppler binaries](http://blog.alivate.com.au/poppler-windows/) and add them to your system PATH

## Usage

Run the script from the command line:

```
python ocr.py path/to/file_or_directory [-o output_file.txt]
```

- `path/to/file_or_directory`: Path to an image file, PDF, or directory containing images/PDFs
- `-o output_file.txt` or `--output output_file.txt`: (Optional) Specify an output file to save the results

### Examples

1. Process a single image file:
   ```
   python ocr.py image.png
   ```

2. Process a single PDF file:
   ```
   python ocr.py document.pdf
   ```

3. Process a directory and save the output to a file:
   ```
   python ocr.py path/to/directory -o results.txt
   ```

## How It Works

1. The script uses the `pytesseract` library, which is a Python wrapper for Google's Tesseract OCR engine, to extract text from images.
2. For PDF files, it uses the `pdf2image` library to convert PDF pages to images, which are then processed by the OCR engine.
3. When processing a directory, it identifies all supported file types and processes them sequentially.
4. The extracted text is either printed to the console or saved to a specified output file.

## Supported File Types

- Images: PNG, JPG, JPEG, TIFF, BMP, GIF
- PDFs

## Troubleshooting

- If you encounter issues with PDF processing, ensure that Poppler is correctly installed and accessible in your system PATH.
- For image processing issues, verify that Tesseract OCR is properly installed and recognized by your system.
- If you're having problems with specific file types, check that they are supported and not corrupted.

## Contributing

Contributions to improve the script or extend its functionality are welcome. Please feel free to submit a pull request or open an issue to discuss potential changes/additions.

## License

This project is open source and available under the [MIT License](LICENSE).# Image-and-PDF-to-Text-Converter
