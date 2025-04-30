Air Quality Prediction Using Machine Learning

Overview:
This project is a complete machine learning pipeline for predicting air quality using environmental sensor data. It starts with data preprocessing and exploratory analysis, builds and compares multiple ML models, and finally deploys the best-performing model through a user-friendly Flask web application.

The web app allows users to input sensor readings (weight, humidity, and temperature) and receive real-time air quality predictions. A clean, responsive interface with a background slideshow and dark mode toggle enhances the usability and visual appeal of the application.

Features:
Data loading and cleaning from CSV files

Merging multiple datasets based on shared identifiers

Exploratory data analysis (EDA) using visualization tools

Model building and evaluation using cross-validation (accuracy and standard deviation)

Web app deployment using Flask

Real-time prediction interface with form inputs

Dark mode toggle and dynamic background slideshow for modern UI

Prediction Inputs:
The model predicts the quality of air based on the following inputs:

Weight (proxy for particulate matter)

Humidity (in percentage)

Temperature (in degrees Celsius)

Example Input for Poor Air Quality:
Weight: 180.0

Humidity: 85.0

Temperature: 38.0

Libraries Used
pandas – Data loading and manipulation

matplotlib – Visualization and EDA

scikit-learn – Model training and evaluation

Flask – Web framework for deployment

Bootstrap – Frontend design framework (for responsive layout)

Installation
Install the required Python libraries:

Installations:
pip install pandas
pip install matplotlib
pip install scikit-learn
pip install Flask
To run the application:

To run the application :
python new_air.py

Future Improvements
Add live sensor data integration or IoT device support

Expand prediction features (e.g., CO2, NO2 levels)

Store prediction history using a backend database

Deploy the app on a cloud platform (like Render or Heroku)

