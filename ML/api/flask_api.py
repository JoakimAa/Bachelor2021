from flask import Flask, request
from PIL import Image
import cv2
import base64
import numpy as np
import io
from ML.Cnn import cnn_predict
from ML.NER import ner_spacy_temp
import os
from dotenv import load_dotenv
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
    print(cnn_predict.classify_image(image))

    #GI BILDE OG PREDICTION TIL OCR HER

    #OCR OUTPUT INN TIL SPACY
    #price, date = ner_spacy_temp(ocr_text)



    return {
        "amount": 97,
        "type": "Kvittering",
        "company": prediction,
        "date": "23.09.2017 10:38"
    }


if __name__ == "__main__":
    #     run flask application in debug mode
    app.run(debug=True, use_reloader=False, port=os.getenv('BASE_PORT'))
