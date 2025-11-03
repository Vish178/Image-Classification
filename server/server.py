from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/clf_img", methods=["GET", "POST"])
def clf_img():
    return "Hello, this is the Image Classification Server!"

if __name__ == '__main__':
    app.run(port = 5000, debug=True)