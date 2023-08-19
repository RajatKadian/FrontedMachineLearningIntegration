from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd

from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS module

app = Flask(__name__)
CORS(app)  #

# Load the trained model from the file
model = joblib.load('trained_model.joblib')

print(model)


sample_data0 = {
    'length': [44.301529],
    'weight': [9.439796e-01],
    'count': [612.683711],
    'looped': [107.881919],
    'neighbors': [2.238271],
    'income': [8.689590e+08]
}

# Create the DataFrame
df_sample = pd.DataFrame(sample_data0)

# predicted_outcome = model.predict(df_sample)
#
# print(predicted_outcome)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    try:
        # Get the input data from the request
        data = request.json['data']

        print(data)

        df_sample = pd.DataFrame(data)

        predicted_outcome = model.predict(df_sample)

        print(predicted_outcome)

        return jsonify({'predictions': predicted_outcome.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
