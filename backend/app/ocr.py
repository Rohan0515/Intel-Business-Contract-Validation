import pytesseract
from PIL import Image
import io

def parse_document(file):
    image = Image.open(io.BytesIO(file.read()))
    text = pytesseract.image_to_string(image)
    return text
