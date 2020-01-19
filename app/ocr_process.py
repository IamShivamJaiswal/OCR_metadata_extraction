import pytesseract
class OCR:

    def __init__(self):
        super().__init__()

    @staticmethod
    def image_to_string(img):
        return pytesseract.image_to_string(img)

    @staticmethod
    def image_to_data(img):
        return pytesseract.image_to_data(img,output_type='data.frame')
