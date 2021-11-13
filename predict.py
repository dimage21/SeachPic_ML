from labels import place_labels
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

def get_predict_result(image):
    result = []
    image = preprocess_img(image)
    features = model.predict(image)
    top_numbers = (-features).argsort()[:3]
    for index in range(3):
        result.append(place_labels[top_numbers[0][index]][1])
    return result
