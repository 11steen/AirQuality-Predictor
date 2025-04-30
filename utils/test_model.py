import joblib

model = joblib.load('air_quality_model.pkl')

#values: [weight, humidity, temperature]
sample = [[20, 50, 22]]  
prediction = model.predict(sample)

print("Prediction:", prediction[0])
