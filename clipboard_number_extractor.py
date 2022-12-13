from PIL import ImageGrab, ImageEnhance
from pytesseract import image_to_string, pytesseract
import clipboard


class Extractor:
    def __init__(self):
        self.ENHANCE_FACTOR = 1.5
        self.image = None
        self.numbers = None

    def __str__(self):
        return f"Numbers found:\n{self.numbers}" if len(self.numbers) > 0 else "No numbers found."

    def enhance_image(self):
        # Increase contrast and sharpness of self.image
        contrast_enhancer = ImageEnhance.Contrast(self.image)
        self.image = contrast_enhancer.enhance(self.ENHANCE_FACTOR)
        sharpness_enhancer = ImageEnhance.Contrast(self.image)
        self.image = sharpness_enhancer.enhance(self.ENHANCE_FACTOR)

    def parse_image(self):
        # Analyze image and extract numbers
        pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        self.numbers = image_to_string(self.image, lang="eng", config="digits").strip()

    def get_clipboard(self):
        # Get the clipboard content
        self.image = ImageGrab.grabclipboard()

    def set_clipboard(self):
        # Set the clipboard content
        clipboard.copy(self.numbers)


def main():
    try:
        extractor = Extractor()
        extractor.get_clipboard()
        extractor.enhance_image()
        extractor.parse_image()
        extractor.set_clipboard()
        print(extractor)

    # The clipboard content is not an image
    except Exception as e:
        print(f"Wrong content in the clipboard! Error found: {e}")


if __name__ == "__main__":
    main()
