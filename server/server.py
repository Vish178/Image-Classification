from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/main")
def main():
    return "Hello, this is the Image Classification Server!"

if __name__ == '__main__':
    app.run(port = 5000, debug=True)