import matplotlib.pyplot as plt
import cv2
import os
import random

BASE_PATH = "testImages"
CATEGORIES = ["flybuss", "neptuntaxi", "trondertaxi"]
IMG_SIZE = 60

for category in CATEGORIES:
    path = os.path.join(BASE_PATH, category)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
        new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
        plt.imshow(new_array, cmap="gray")
        plt.show()


