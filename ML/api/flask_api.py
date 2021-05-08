from flask import Flask, request
from PIL import Image
import cv2
import base64
import numpy as np
import io
from Cnn import cnn_predict

app = Flask(__name__)
version = "v1"


def base64_converter(base64_string):
    img_data = base64.urlsafe_b64decode(base64_string)
    image = Image.open(io.BytesIO(img_data))
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)


def base64_decode(request):
    request_data = request.data
    image_base64_decode = base64.urlsafe_b64decode(request_data)
    return base64_converter(image_base64_decode)


@app.route(f"/{version}/api/")
def hello():
    return "Home"


@app.route(f"/{version}/api/upload", methods=["POST"])
def api_1():
    image = base64_converter(request.data)
    print(image)
    print(cnn_predict.classify_image(image))

    return {
        "amount": 97,
        "type": "Kvittering",
        "company": "Entur",
        "date": "23.09.2017 10:38"
    }


if __name__ == "__main__":
    #     run flask application in debug mode
    app.run(debug=True, use_reloader=False, port=5002)
