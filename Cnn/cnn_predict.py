from tensorflow.keras.models import load_model
import numpy as np
import cv2

CATEGORIES = ["flybuss", "neptuntaxi", "trondertaxi"]
IMG_SIZE = 60
TEST_DIR = "testImages"

img_array = cv2.imread("testImages/flybuss/2018-04-15 Flybuss Rygge-OSL__trans150_50.JPG", cv2.IMREAD_GRAYSCALE)
img_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
img_array = np.array(img_array).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

model = load_model("models/my_model")

prediction_array = model.predict(img_array)[0]
predicted_category = CATEGORIES[np.argmax(prediction_array)]

print(prediction_array)
print(predicted_category)
