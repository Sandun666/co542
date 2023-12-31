# import
import base64
import numpy as np
from flask import Flask, request, jsonify, render_template
from PIL import Image
import pickle
import io
import os
from skimage.color import rgb2gray
from skimage.transform import resize

app = Flask(__name__)
model = pickle.load(open('models/cats_and_dogs.pkl','rb'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if 'img' not in request.files:
        return 'No file'
    file = request.files['img'].read()
    npimg = np.frombuffer(file, np.uint8)
    img = Image.open(io.BytesIO(npimg))
    img_gray = rgb2gray(img)
    img_resized = resize(img_gray, (64, 64), anti_aliasing=True)
    img_array = np.reshape(img_resized, (1, 64, 64, 1))
    predictions = model.predict(img_array)

    # Convert the prediction to a binary label (0 or 1)
    predicted_label = 1 if predictions[0, 0] > 0.5 else 0

    class_name = "Cat" if predicted_label == 1 else "Dog"

    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return render_template("predict.html", prediction=class_name, uploaded_image=img_str)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)