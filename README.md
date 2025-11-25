# Celebrity Face Classifier
![alt text](https://github.com/Vish178/Image-Classification/blob/master/front_end/thumnails/Screenshot.png)
## Project Overview
This project is a web-based celebrity face recognition/classification system. It uses deep learning (FaceNet embeddings + a custom MLP classifier) to identify celebrities from uploaded images. The frontend is built with HTML, CSS, and JavaScript, while the backend uses Flask and Keras/TensorFlow.

## How the Model Works
1. **Face Detection & Preprocessing:**
   - Uploaded images are processed using OpenCV to detect faces and eyes.
   - The detected face is cropped and converted to RGB, resized to 160x160 pixels.
2. **Embedding Extraction:**
   - The cropped face is passed to a pre-trained FaceNet model to extract a 128-dimensional embedding vector.
3. **Classification:**
   - The embedding is fed into a trained MLP (Multi-Layer Perceptron) classifier.
   - The classifier outputs confidence scores for each celebrity class.
   - The celebrity with the highest confidence is selected as the prediction.
4. **Frontend Display:**
   - The frontend shows the predicted celebrity's image and name, along with a table of confidence scores for all classes.

## Installation & Setup
### 1. Clone the Repository
```bash
# Clone the repo
https://github.com/<your-username>/Image-Classification.git
cd Image-Classification
```

### 2. Create & Activate Python Environment
It is recommended to use Conda or venv.
```bash
# Using conda
conda create -n img_gen python=3.8
conda activate img_gen
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
If you don't have a `requirements.txt`, install manually:
```bash
pip install flask flask-cors keras tensorflow keras-facenet opencv-python numpy
```

### 4. Prepare Artifacts
- Place the trained model file (`face_classifier_model.h5`) and `class_dictionary.json` in the `artifacts/` directory.
- Haar cascade XML files should be in `server/haar_cacades/`.

### 5. Run the Backend Server
```bash
cd server
python server.py
```
The Flask server will start at `http://127.0.0.1:5000`.

### 6. Run the Frontend
You must serve the frontend via a local web server (not file://).
```bash
cd front_end
python -m http.server 8080
```
Open `http://localhost:8080/app.html` in your browser.

## Usage
- Upload an image using the web interface.
- Click "Classify".
- The app will show the predicted celebrity and confidence scores for all classes.

## Troubleshooting
- If you see CORS errors, ensure Flask-CORS is installed and enabled in `server.py`.
- If you get `413 Request Entity Too Large`, increase `MAX_CONTENT_LENGTH` in Flask config.
- If face/eyes are not detected, try a clearer image.

## Brief Description
This project demonstrates a practical application of deep learning for face recognition, combining FaceNet embeddings with a custom classifier and a user-friendly web interface. It is suitable for learning, demos, or as a base for more advanced face recognition systems.


Inspired by:  
[![IMAGE ALT TEXT HER](https://img.youtube.com/vi/qWXXHjV3JHI/0.jpg)](https://www.youtube.com/watch?v=qWXXHjV3JHI)
---
---
Dataset Used: https://www.kaggle.com/datasets/vishesh1412/celebrity-face-image-dataset/data
---
---
For questions or contributions, please open an issue or pull request.
---
