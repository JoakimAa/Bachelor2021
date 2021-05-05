import numpy as np
import os
import cv2
import random
import pickle

DATADIR = "C:\Datasets\simpdata_labeled"
CATEGORIES = ["flybuss", "neptuntaxi", "trondertaxi"]
IMG_SIZE = 60


def create_training_data():
    training_data = []
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        category_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, category_num])
            except Exception as e:
                pass
    random.shuffle(training_data)
    return training_data


def xy_split(data):
    X = []
    y = []
    for features, label in data:
        X.append(features)
        y.append(label)
    X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    return X, y


def xy_save(X, y):
    pickle_out = open("pickledDataset/X.pickle", "wb")
    pickle.dump(X, pickle_out)
    pickle_out.close()

    pickle_out = open("pickledDataset/y.pickle", "wb")
    pickle.dump(y, pickle_out)
    pickle_out.close()


training_data = create_training_data()
X, y = xy_split(training_data)
xy_save(X, y)
