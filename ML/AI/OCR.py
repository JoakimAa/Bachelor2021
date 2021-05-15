import cv2
import pytesseract
import re
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('templates/trondertaxi.jpg')
#template = cv2.imread("out/template.jpg")
img_S = cv2.resize(img, None, fx=1, fy=0.8, interpolation=cv2.INTER_AREA)
#img_T = cv2.resize(template, None, fx=1, fy=0.9, interpolation=cv2.INTER_AREA)

grayImg = cv2.cvtColor(img_S, cv2.COLOR_BGR2GRAY)
adaptive_thresholdImg = cv2.adaptiveThreshold(grayImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41, 17)


NOR = 'nor'
config = "--psm 4"
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_data(adaptive_thresholdImg, lang=NOR, config=config)


# #[   0          1           2           3           4          5         6       7       8        9        10      11  ]
# #['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height', 'conf', 'text']

print(pytesseract.get_languages(config=''))
print(boxes)

detectedWords = []
for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img_S, (x, y), (w + x, h + y), (0, 0, 255), 1)
            cv2.putText(img_S, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (25, 25, 255), 1)
            detectedWords.append(b[11])


for word in detectedWords:
    if(re.search("([0-9]{2}([.]|/|-)[0-9]{2}([.]|/|-)[0-9]{4})", word)):
        date = word
        print("Dato: ", date)
        break
    else:
        print("Date not found")

print(detectedWords)
cv2.imshow('adaptive_img', adaptive_thresholdImg)
cv2.imshow('result', img_S)
#cv2.imshow("template", img_T)
cv2.waitKey(0)

output_string = ", ".join(detectedWords)




