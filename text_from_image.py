from PIL import Image
from pytesseract import pytesseract
import numpy as np

def pil_from_np(img: np.array)-> Image:
    pil_img = Image.fromarray(np.uint8(img * 255) , 'L')
    return pil_img


def extract_text(image: Image, lang: str = "eng")-> str:
    img = image

    extracted_text = pytesseract.image_to_string(img, lang=lang)

    return extracted_text
