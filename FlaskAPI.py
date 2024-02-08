import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

def load_models():
    models = {}
    model_paths = {
        "model1": "svc_model.pkl",
        "model2": "model2.pkl",
        "model3": "model3.pkl",
        "model4": "model4.pkl"
    }

    for model_id, model_path in model_paths.items():
        with open(model_path, "rb") as file:
            model = pickle.load(file)
            models[model_id] = model

    return models

# Define the API endpoint for the GET request
@app.route("/prediction", methods=["GET"])
def get_prediction():
    #features = [float(request.args.get(feat)) for feat in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]

    sepal_length = float(request.args.get('sepal_length'))
    sepal_width = float(request.args.get('sepal_width'))
    petal_length = float(request.args.get('petal_length'))
    petal_width = float(request.args.get('petal_width'))
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    input_data = scaler.transform(input_data)    
    
    models = load_models()

    predictions = {}
    for model_id, model in models.items():
        prediction = model.predict(input_data)
        predictions[model_id] = prediction[0]

    return jsonify(predictions), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)