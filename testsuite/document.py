try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
from string_atomizer import StringAtomizer

def main():
    abcd=pytesseract.image_to_string(Image.open('hangul.png'), lang='kor') # OCR
    sa = StringAtomizer()
    result = sa.atomizeString(abcd)
    
    print(result)

if __name__ == '__main__':
    main()


