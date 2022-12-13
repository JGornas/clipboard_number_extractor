# Extractor

The Extractor script is a simple Python program that can be used to extract numbers from an image in the clipboard, and insert these numbers back into the clipboard.
## Requirements

The Extractor script requires the following Python packages:

    PIL
    pytesseract
    clipboard

These packages can be installed using pip:

`pip install PIL`
`pip install pytesseract`
`pip install clipboard`

## Usage

To use the Extractor script, simply run the main.py file:

`python main.py`

This will create an Extractor object, get the clipboard content, enhance the image, extract numbers from the image, and set the numbers to the clipboard. If no image is found in the clipboard, an error message will be printed.
## License

The Extractor script is licensed under the MIT License.