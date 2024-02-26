import os
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2
from keras.models import load_model
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

basepath = os.path.dirname(__file__)

model_path = os.path.join(basepath, 'BrainTumor10Epochs.h5')
model = load_model(model_path)
print('Model loaded. Check http://127.0.0.1:5000/')

def get_className(classNo):
	if classNo == 0:
		return "No Brain Tumor Detected 😀"
	elif classNo == 1:
		return "Yes Brain Tumor Detected 😞"
      
def getResult(img_path):
    # Extract the filename from the path
    filename = os.path.basename(img_path)

    # Check if the filename indicates it is from the dataset
    if filename.startswith('pred'):

        # Read the image using OpenCV
        image = cv2.imread(img_path)

        # Convert the image to RGB format using PIL
        image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        # Resize the image to the required input size
        image = image.resize((64, 64))

        # Convert the image to a NumPy array
        image = np.array(image)

        # Expand the dimensions to create a batch of size 1
        input_img = np.expand_dims(image, axis=0)

        # Make predictions using the model
        predictions = model.predict(input_img)

        # Print the entire array of predictions for debugging
        print("Predictions:", predictions)

        # Adjust the threshold based on your observations
        threshold = 0.5
        predicted_class_index = 1 if predictions[0, 0] > threshold else 0

        # Print the predicted class index for debugging
        print("Predicted Class Index (After Threshold):", predicted_class_index)

        return predicted_class_index
    else:
        # If the file is not from the dataset, return a message
        print("File Is Not From The Dataset.")
        return None

# def getResult(img):
#     image = cv2.imread(img)
#     image = Image.fromarray(image, 'RGB')
#     image = image.resize((64, 64))
#     image = np.array(image)
#     input_img = np.expand_dims(image, axis = 0)
#     result = np.argmax(model.predict(input_img), axis = 1)
#     return result

@app.route('/', methods = ['GET'])
def index():
    # return render_template('index.html')
    return render_template('index.html', result=index)

uploads_dir = os.path.join(basepath, 'uploads')
os.makedirs(uploads_dir, exist_ok=True)

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        # Get the result from the model
        value = getResult(file_path)

        if value is not None:
        # If the result is valid, display the corresponding class name
            result = get_className(value) 
            return result
        else:
            # If the file is not from the dataset, return an appropriate message
            return "Invalid File. Please Upload An MRI Scanned Image." 
        
    return None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)