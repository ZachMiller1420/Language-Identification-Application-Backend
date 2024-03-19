from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Load your machine learning model
global Lrdetect_Model
with open('model.pckl', 'rb') as model_file:
    Lrdetect_Model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    data = request.get_json()
    text = data['text']
    
    # Perform prediction using your machine learning model
    prediction = Lrdetect_Model.predict([text])[0]
    
    # Return prediction as JSON
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)

