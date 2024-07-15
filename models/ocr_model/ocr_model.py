import pytesseract
from PIL import Image

def ocr_model(image):
    text = pytesseract.image_to_string(image)
    return text

if __name__ == "__main__":
    from PIL import Image
    import io

    # Create a blank white image for testing
    image = Image.new('RGB', (100, 100), color=(255, 255, 255))
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    text = ocr_model(Image.open(img_byte_arr))
    print("OCR Output:", text)
