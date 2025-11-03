from flask import Flask, request, jsonify
import utils
app = Flask(__name__)

@app.route("/predict", methods=["GET", "POST"])
def predict():
    image_data = request.form['image_data']

    response = jsonify(utils.predict(image_data))

if __name__ == '__main__':
    utils.load_saved_artifacts()
    app.run(port = 5000, debug=True)