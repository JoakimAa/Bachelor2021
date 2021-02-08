import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('..\\images\\DaU9KXqWkAA-eVA.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
grayImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
adaptive_trhesholdImg = cv2.adaptiveThreshold(grayImg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 85, 11)

config = "--psm 4"
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_data(adaptive_trhesholdImg, lang='nor', config=config)
print(pytesseract.get_languages(config=''))
print(boxes)

for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 3)
            cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

cv2.imshow('result', img)
cv2.waitKey(0)
