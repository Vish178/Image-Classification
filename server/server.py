from flask import Flask, request, jsonify 
import utils

app = Flask(__name__)

@app.route("/predict", methods=["GET", "POST"])
def predict():
    image_data = request.form['image_data']
    result = utils.predict(b64_data=image_data)
    if result is None:
        response = jsonify({'error': 'Face or eyes not detected'})
    else:
        response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    utils.load_saved_artifacts()
    app.run(port = 5000, debug=True)