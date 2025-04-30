Air Quality Prediction Using Machine Learning

Overview:

This project implements a complete machine learning pipeline for predicting air quality based on environmental sensor data. The pipeline includes data preprocessing, exploratory analysis, model building, and deployment of the best-performing model through a Flask-based web application.

The web app allows users to input sensor readings (weight, humidity, and temperature) and receive real-time air quality predictions. The user interface is clean, responsive, and modern, featuring a dynamic background slideshow and a dark mode toggle for enhanced usability and visual appeal.

Features:

Data Loading and Cleaning: Efficiently loads and cleans sensor data from CSV files.

Merging Datasets: Combines multiple datasets based on shared identifiers to provide a comprehensive dataset.

Exploratory Data Analysis (EDA): Visualizes key data characteristics to gain insights into trends and relationships.

Model Building and Evaluation: Trains multiple machine learning models, evaluates them using cross-validation (accuracy and standard deviation), and selects the best performer.

Web App Deployment: Deploys the best model through a Flask web application for easy user interaction.

Real-Time Prediction Interface: Users input sensor data and instantly receive air quality predictions.

Dark Mode and Slideshow Background: Toggle between light and dark modes, with a dynamic slideshow background for a modern, sleek design.

Prediction Inputs:

The air quality is predicted based on the following user inputs:

Weight: Proxy for particulate matter (in arbitrary units)

Humidity: Percentage of moisture in the air

Temperature: Temperature in degrees Celsius

Example Input for Poor Air Quality:

Weight: 180.0

Humidity: 85.0

Temperature: 38.0

Libraries Used:

pandas: For data loading, manipulation, and cleaning.

matplotlib: For creating visualizations and performing EDA.

scikit-learn: For training and evaluating machine learning models.

Flask: For web framework deployment and serving the prediction interface.

Bootstrap: For building a responsive and attractive frontend design.

Installation:

To set up the project on your local machine, follow these steps:

Install the required Python libraries:

bash
pip install pandas
pip install matplotlib
pip install scikit-learn
pip install Flask

Run the application: 

bash
python new_air.py


Future Improvements:

Live Sensor Data Integration: Add support for real-time data input from IoT devices or environmental sensors.

Expand Prediction Features: Integrate additional features such as CO2, NO2, and other pollutant levels.

Prediction History Storage: Store past predictions and user inputs using a backend database.

Cloud Deployment: Deploy the app to a cloud platform like Heroku or Render for easy access and scalability.



