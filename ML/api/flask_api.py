from flask import Flask, request
from PIL import Image
import cv2
import base64
import numpy as np
import io
from AI.main import return_data
from Cnn import cnn_predict
import os
from dotenv import load_dotenv
from NER import ner_spacy_temp
from NER.ner_spacy_temp import run_spacy
load_dotenv()

app = Flask(__name__)


def base64_converter(base64_string):
    img_data = base64.urlsafe_b64decode(base64_string)
    image = Image.open(io.BytesIO(img_data))
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)


@app.route(f"/{os.getenv('API_VERSION')}")
def home():
    return "Home"


@app.route(f"/{os.getenv('API_VERSION')}/upload", methods=["POST"])
def post_image():
    image = base64_converter(request.data)
    print(image)
    prediction = cnn_predict.classify_image(image)
    print(prediction)
    ocr_data = return_data(image, prediction)
    price, date = run_spacy(ocr_data)

    return {
        "amount": price,
        "type": "Kvittering",
        "company": prediction,
        "date": date
    }


if __name__ == "__main__":
    #     run flask application in debug mode
    app.run(debug=True, use_reloader=False, port=os.getenv('BASE_PORT'))
