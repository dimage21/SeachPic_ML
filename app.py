from flask import Flask
import flask
from PIL import Image
import io
from predict import get_predict_result
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}
    if flask.request.files.get("image"):
        image = flask.request.files["image"].read()
        image = Image.open(io.BytesIO(image))
        result = get_predict_result(image)
        data["success"] = True
        data["data"] = result
        return flask.jsonify(data), 200
    return flask.jsonify(data),404


if __name__ == '__main__':
    app.run()
