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

def load_test_data():
    test_data = []
    for category in CATEGORIES:
        path = os.path.join(TEST_DIR, category)
        category_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                img_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                test_data.append([img_array, category_num])
            except Exception as e:
                pass
        return test_data

test_data = load_test_data();
np.set_printoptions(threshold=np.inf)
print(test_data[0][2])
#img_array = np.array(img_array).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
#model = load_model("models/my_model")
#test = model.predict())

#print(test)


