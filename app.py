from flask import Flask
from PIL import Image
import io
import os
from predict import get_predict_result
from flask import request
from flask import g
import flask
import logging
import time

app = Flask(__name__)
app.logger.setLevel(logging.INFO)


@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}
    location_type = request.args.get('type')
    if request.files.get("image"):
        image = request.files["image"].read()
        image = Image.open(io.BytesIO(image))
        result = get_predict_result(image, location_type)
        data["success"] = True
        data["data"] = result
        return flask.jsonify(data), 200
    return flask.jsonify(data), 404


@app.before_request
def before_request():
    g.start = time.time()
    app.logger.info(" Request: {}".format(request.full_path))


@app.after_request
def after_request(response):
    execution_time = time.time() - g.start
    app.logger.info(" Response: status_code = {}, time = {}".format(response.status_code, execution_time))
    return response


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)