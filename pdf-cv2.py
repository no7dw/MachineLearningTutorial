import sys
import pytesseract
import cv2
import pdfplumber

def main(argv):
    input_file=''
    print(sys.argv)
    input_file = sys.argv[1]
    pdf= pdfplumber.open(input_file)
    p = pdf.pages[0]
    img0 = p.to_image()
    output_file = "./tmp.png"
    img0.save( output_file , format="PNG")
    img = cv2.imread(output_file, cv2.IMREAD_GRAYSCALE) 
    imgx =  img[0:100, 0:250]
    cv2.imwrite("./tmp_rect.png", imgx)
    text  = pytesseract.image_to_string(imgx)
    print(text)

if __name__ == '__main__':
    main(sys.argv)
