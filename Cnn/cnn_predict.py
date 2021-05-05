import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import normalize, to_categorical
from sklearn.model_selection import train_test_split
import pickle
import numpy as np
import cv2
import os

CATEGORIES = ["flybuss","neptuntaxi", "trondertaxi"]
IMG_SIZE = 60
TEST_DIR = "testImages"

img_array = cv2.imread("testImages/flybuss/flybuss_test.JPG", cv2.IMREAD_GRAYSCALE)
img_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))


img_array = np.array(img_array).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
model = load_model("models/my_model")
test = model.predict()

print(test)


