# import
import numpy as np
from flask import Flask, request, jsonify, render_template
from PIL import Image
import pickle
import io
import os

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
    img = img.resize((64, 64))
    img_array = np.array(img) / 255.0  # Normalize pixel values to be between 0 and 1
    img_array = np.reshape(img_array, (1, 64, 64))  # Reshape to match the model input shape
    predictions = model.predict(img_array)

    # Convert the prediction to a binary label (0 or 1)
    predicted_label = 1 if predictions[0, 0] > 0.5 else 0

    return jsonify(int(predicted_label))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)