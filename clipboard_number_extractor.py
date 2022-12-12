from PIL import ImageGrab, ImageEnhance
from pytesseract import image_to_string, pytesseract


def main():
    # Check if the clipboard content is an image
    try:
        # Get the clipboard content
        image = ImageGrab.grabclipboard()
        image.save('clipboard.png', 'PNG')

        # Increase contrast and sharpness
        factor = 1.5
        contrast_enhancer = ImageEnhance.Contrast(image)
        image_output = contrast_enhancer.enhance(factor)
        sharpness_enhancer = ImageEnhance.Contrast(image_output)
        image_output = sharpness_enhancer.enhance(factor)

        # Parse image with tesseract
        pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        numbers = image_to_string(image_output, lang="eng", config="digits")

        # Print the numbers
        print(f"Numbers found:\n{numbers}" if len(numbers) > 0 else "No numbers found")

    # The clipboard content is not an image
    except Exception as e:
        print(f"No file in clipboard! Error found: {e}")
        exit()


if __name__ == "__main__":
    main()
