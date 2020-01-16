
from PIL import Image
import PIL.Image
import cv2
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
# TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'
filename = 'media/knitking_magazine_vol_15_no.6-12.png'
img = PIL.Image.open(filename)

img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print('Original Dimensions : ', img.shape)

imS = cv2.resize(img, (1350, 1150))
cv2.imshow("output",imS)
cv2.imwrite('Output Image.PNG', imS)
cv2.waitKey(0)
output = pytesseract.image_to_string(imS, lang='eng')
print(output)
