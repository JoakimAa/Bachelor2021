import pytesseract
import cv2
import matplotlib.pyplot as plt
import os

BASE_PATH = "testImages"
CATEGORIES = ["flybuss.JPG", "neptun.jpg", "tronder.JPG"]

for category in CATEGORIES:
    path = os.path.join(BASE_PATH, category)
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    rescaled_width = int(img.shape[1] * 0.5)
    rescaled_height = int(img.shape[0] * 0.5)
    dim = (rescaled_width, rescaled_height)
    img = cv2.resize(img, dim)

    gaus_thres = cv2.adaptiveThreshold(
        img,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        10)

    img_string = pytesseract.image_to_string(img)
    text_path = os.path.join("OcrOutputs", category.split(".")[0] + ".txt")
    text_file = open(text_path, "w")
    text_file.write(img_string)
    text_file.close()

    print("----------IMAGE TO STRING: ", category, "-----------")
    print(img_string)
    plt.imshow(gaus_thres, cmap="gray")
    plt.show()
