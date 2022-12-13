from PIL import ImageGrab, ImageEnhance
from pytesseract import image_to_string, pytesseract
import clipboard


class Extractor:
    """
    Extractor is a class that can be used to extract numbers from an image in the clipboard and insert these numbers
    back in to the clipboard.

    Attributes:
        image (PIL.Image): The image to be processed.
        numbers (str): The numbers found in the image.

    Methods:
        get_clipboard: Get the clipboard content and set it as the image to be processed.
        enhance_image: Enhance the contrast and sharpness of the image.
        parse_image: Analyze the image and extract numbers from it.
        set_clipboard: Set the numbers found in the image to the clipboard.
    """

    def __init__(self):
        self.image = None
        self.numbers = None

    def __str__(self) -> str:
        return f"Numbers found:\n{self.numbers}" if self.numbers else "No numbers found."

    def enhance_image(self, enhance_factor: float = 1.5):
        contrast_enhancer = ImageEnhance.Contrast(self.image)
        self.image = contrast_enhancer.enhance(enhance_factor)
        sharpness_enhancer = ImageEnhance.Contrast(self.image)
        self.image = sharpness_enhancer.enhance(enhance_factor)

    def parse_image(self):
        pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        self.numbers = image_to_string(self.image, lang="eng", config="digits").strip()

    def get_clipboard(self):
        self.image = ImageGrab.grabclipboard()

    def set_clipboard(self):
        clipboard.copy(self.numbers)


def main():
    """
    This function creates an Extractor object, gets the clipboard content, enhances the image,
    extracts numbers from the image, and sets the numbers to the clipboard.
    If no image is found in the clipboard, an error message is printed.
    """
    try:
        extractor = Extractor()
        extractor.get_clipboard()
        extractor.enhance_image()
        extractor.parse_image()
        extractor.set_clipboard()
        print(extractor)
    except AttributeError:
        print("No image in clipboard.")


if __name__ == "__main__":
    main()
