from flask import Flask, render_template, request
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
import webbrowser
from threading import Timer

app = Flask(__name__)

# Load and prepare data
def load_data():
    sensor_data = pd.read_csv("sensor_data.csv")
    quality_data = pd.read_csv("quality_control_data.csv")
    rawdataset = sensor_data.merge(quality_data, on="prod_id")
    dataset = rawdataset.drop(columns='prod_id')
    return dataset

# Prepare features and target
def prepare_data(dataset):
    X = dataset.iloc[:, 0:3]  
    Y = dataset.iloc[:, 3]  
    return X, Y

# Load the saved model
model = joblib.load('air_quality_model.pkl')


@app.route('/')
def home():
    return render_template('index.html', prediction_text="")

@app.route('/predict', methods=['POST'])
def predict():
    try:

        testWeight = float(request.form['weight'])
        testHumidity = float(request.form['humidity'])
        testTemperature = float(request.form['temperature'])

        prediction = model.predict([[testWeight, testHumidity, testTemperature]])[0]

        if prediction == 1:
            result = "Air Quality: Good"
        else:
            result = "Air Quality: Poor"

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        print(f"Error occurred: {e}")
        return render_template('index.html', prediction_text="Error: Unable to process your request. Please try again.")

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    Timer(1, open_browser).start()  # to open our browser in less time
    app.run(debug=True)
