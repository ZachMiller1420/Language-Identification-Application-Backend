from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

MODEL_PATH = 'model.pckl'

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']
    # Perform prediction using your machine learning model
    # prediction = model.predict(text)
    # Replace 'Your prediction here' with the actual prediction
    return jsonify({'prediction': 'Your prediction here'})

if __name__ == '__main__':
    app.run(debug=True)
