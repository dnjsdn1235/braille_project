-*- coding: utf-8 -*-
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import argparse
from jamostoolkit import JamosSeparator

abcd=pytesseract.image_to_string(Image.open('hangul.png'), lang='kor') # OCR

parser = argparse.ArgumentParser(description='Jamos toolkit')
parser.add_argument('--string', default=abcd, help='Please enter the string you want to separator.$
args = parser.parse_args()

def main():
    jamos = JamosSeparator(args.string)
    jamos.run()
    print(format(args.string))
    print(format(jamos.get()))
    
    print(format(jamos.get())[1])
    print(format(jamos.get())[2])
    print(format(jamos.get())[3])
    print(format(jamos.get())[4])
    print(format(jamos.get())[5])
    print(format(jamos.get())[6])
    print(format(jamos.get())[7])
    print(format(jamos.get())[8])
    print(format(jamos.get())[9])
    print(format(jamos.get())[10])

if __name__ == '__main__':
    main()


