import io
from app.ocr import parse_document
from PIL import Image

def test_parse_document():
    image = Image.new('RGB', (100, 100), color = (255, 255, 255))
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    text = parse_document(img_byte_arr)
    assert text == ''  