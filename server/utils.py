import cv2
import base64
import numpy as np
import json
from keras.models import load_model
from keras_facenet import FaceNet

__class_name_to_number = None
__class_number_to_name = None

__embedder = None
__model = None


def predict(path = None, b64_data = None, ):

    img_rgb = detect_face_and_eyes(path, b64_data)

    if img_rgb is None:
        print("Image not found or face/eyes not detected.")
        return None
    
    embed = __embedder.embeddings([img_rgb])[0]

    pred = __model.predict(np.expand_dims(embed, axis=0))[0]
    label_map_rev = {v: k for k, v in __class_name_to_number.items()}
    confidences = {label_map_rev[idx]: float(conf) for idx, conf in enumerate(pred)}

    return confidences

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __class_name_to_number
    global __class_number_to_name

    with open("artifacts/class_dictionary.json", "r") as f:
        __class_name_to_number = json.load(f)
        __class_number_to_name = {v:k for k,v in __class_name_to_number.items()}

    global __model
    global __embedder
    if __model is None:
        __embedder = FaceNet()
        __model = load_model('artifacts/face_classifier_model.h5')
        __model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    print("loading saved artifacts...done")

def b64_to_image(b64_str):

    encoded_data = b64_str.split(',')[1] if ',' in b64_str else b64_str
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def get_b64():
    with open("b64.txt") as f:
        return f.read() 
    
def detect_face_and_eyes(path, b64_data):

    eyes_cascade = cv2.CascadeClassifier("haar_cacades/haarcascade_eye.xml")
    faces_cascade = cv2.CascadeClassifier("haar_cacades/haarcascade_frontalface_alt2.xml")

    
    if path:
        img = cv2.imread(path)
    else:
        img = b64_to_image(b64_data)
        
    faces = faces_cascade.detectMultiScale(img, 1.3, 5)
    
    for (x, y, w, h) in faces:
        img_face = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cropped_face = img_face[y:y + h, x:x + w]
        
        eyes = eyes_cascade.detectMultiScale(cropped_face)
        
        if len(eyes) >= 2:
            cropped_face_rgb = cv2.cvtColor(cropped_face, cv2.COLOR_BGR2RGB)
            return cv2.resize(cropped_face_rgb, (160, 160))
    return None
    
if __name__ == '__main__':
    load_saved_artifacts()
    print(predict(path="jackman-hugh.jpg"))