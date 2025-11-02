import cv2
import base64
import numpy as np
import pywt

def haar_transform(image, mode='haar', level=1):
    img_array = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert to grayscale

    img_array = np.float32(img_array) / 255.0 # Converting to float and Normalize the image

    coeffs = pywt.wavedec2(img_array, mode, level) # Apply Haar Wavelet Transform
    coeffs_H = list(coeffs)
    coeffs_H[0] *= 0 # Set Approximation coefficients to zero

    h_img = pywt.waverec2(coeffs_H, mode) # Reconstruct the image using modified coefficients
    h_img = h_img * 255
    h_img = np.uint8(h_img)

    return h_img

def clf_img(b64_str, file_path=None):
    images = detect_face_and_eyes(file_path, b64_str)
    for img in images:
        scaled_img = cv2.resize(img, (64, 64)) # Resize to 32x32
        
        haar_img = haar_transform(scaled_img)
        haar_img = cv2.resize(haar_img, (64, 64)) # Resize to 32x32 

        combined = np.vstack((scaled_img.reshape(64*64*3,1), haar_img.reshape(64*64,1))) # combine original and haar images
        final_img = combined.reshape(1, 64*64*3 + 64*64).astype(float) # Reshape for model input

def b64_to_image(b64_str):
    encoded_data = b64_str.split(',')[1] if ',' in b64_str else b64_str
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def get_b64():
    with open("b64.txt") as f:
        return f.read() 
    
def detect_face_and_eyes(path, b64_str):

    faces_cascade = cv2.CascadeClassifier("server/haar_cacades/haarcascade_frontalface_alt2.xml")
    eyes_cascade = cv2.CascadeClassifier("server/haar_cacades/haarcascade_eye.xml")

    if path:
        img = cv2.imread(path)
    else:
        img = b64_to_image(b64_str)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
    faces = faces_cascade.detectMultiScale(gray_img, 1.3, 5)

    for (x, y, w, h) in faces:
        img_face = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cropped_gray = gray_img[y:y + h, x:x + w]
        cropped_face = img_face[y:y + h, x:x + w]

        eyes = eyes_cascade.detectMultiScale(cropped_gray)
        if len(eyes) >= 2:
            return cropped_face
    
if __name__ == '__main__':
    print(clf_img(get_b64()), None)