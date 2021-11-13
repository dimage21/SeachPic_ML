import cv2
from labels import place_labels
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('./model/model.h5')

def preprocess_img(image):
    if image.mode != "RGB":
        image = image.convert("RGB")

    image = np.array(image, dtype=np.float32)
    image = cv2.resize(image, (224, 224))
    image = np.expand_dims(image, 0)
    image = image / 255
    return image

def get_predict_result(image):
    result = []
    image = preprocess_img(image)
    features = model.predict(image)
    top_numbers = (-features).argsort()[:3]
    for index in range(3):
        result.append(place_labels[top_numbers[0][index]][1])
    return result
