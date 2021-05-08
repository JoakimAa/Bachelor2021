import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import cv2

CATEGORIES = ["flybuss", "neptuntaxi", "trondertaxi"]
IMG_SIZE = 60
MODEL = "../Cnn/models/my_model"


def classify_image(image):
    physical_devices = tf.config.experimental.list_physical_devices('GPU')
    if len(physical_devices) > 0:
       tf.config.experimental.set_memory_growth(physical_devices[0], True)

    img_array = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
    img_array = np.array(img_array).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

    model = load_model(MODEL)

    prediction_array = model.predict(img_array)[0]

    return CATEGORIES[np.argmax(prediction_array)]

# img_array = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
# img_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
# img_array = np.array(img_array).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
# TEST_DIR = "testImages"
# TEST_IMG_T = "testImages/trondertaxi/tronder_test.JPG"
# TEST_IMG_F = "testImages/flybuss/flybuss_test.JPG"
# TEST_IMG_N = "testImages/neptuntaxi/neptun_test.jpg"
