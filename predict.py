from labels import *
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

model = load_model('./model/model.h5')


def preprocess_img(image):
    if image.mode != "RGB":
        image = image.convert("RGB")
    img = image.resize((224, 224), Image.ANTIALIAS)
    image = np.expand_dims(img, 0)
    image = image / 255.0
    return image


def get_predict_result(image, location_type):
    image = preprocess_img(image)
    features = model.predict(image)
    sorted_similar_idx = (-features).argsort()[:3]
    result = get_filtered_result(location_type, sorted_similar_idx)
    return result


def get_filtered_result(location_type, top_numbers):
    result = []
    index = 0
    while len(result) < 3:
        search_target = place_labels[top_numbers[0][index]]
        if (location_type == "cafe" and not search_target[0] in cafes) or (
                location_type == "attraction" and not search_target[0] in attractions):
            index += 1
            continue
        result.append(search_target[1])
        index += 1
    return result
