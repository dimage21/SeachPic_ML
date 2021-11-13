from flask import Flask
from PIL import Image
import os
import io
from predict import get_predict_result
from flask import request
import flask
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}
    if request.files.get("image"):
        image = request.files["image"].read()
        image = Image.open(io.BytesIO(image))
        result = get_predict_result(image)
        data["success"] = True
        data["data"] = result
        return flask.jsonify(data), 200
    return flask.jsonify(data),404