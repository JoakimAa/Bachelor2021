
from flask import Flask
from PIL import Image
import cv2
import base64
import numpy as np
import io
import cnn_predict

app = Flask(__name__)

def base64_converter(base64_string):
    img_data = base64.b64decode(str(base64_string))
    image = Image.open(io.BytesIO(img_data))
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

@app.route("/post_image", methods=["POST"])
def post_image(base64_string):
    image = base64_converter(base64_string)
    return cnn_predict.classify_image(image)


if __name__ == "__main__":
    #     run flask application in debug mode
    app.run(debug=True, port=5002)