import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

# Load datasets
sensor_data = pd.read_csv("sensor_data.csv")
quality_data = pd.read_csv("quality_control_data.csv")

# Merging datasets
rawdataset = sensor_data.merge(quality_data, on="prod_id")
dataset = rawdataset.drop(columns='prod_id')

print("\nClass distribution:\n", dataset['quality'].value_counts())

# Prepare features and labels
X = dataset[['weight', 'humidity', 'temperature']]
Y = dataset['quality']

# Split data
X_train, X_validation, Y_train, Y_validation = train_test_split(
    X, Y, test_size=0.2, random_state=42, stratify=Y
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_validation_scaled = scaler.transform(X_validation)

# Train model
model = LogisticRegression(class_weight='balanced', solver='liblinear')
model.fit(X_train_scaled, Y_train)

# Evaluate model
predictions = model.predict(X_validation_scaled)
print("\nAccuracy:", accuracy_score(Y_validation, predictions))
print("\nConfusion Matrix:\n", confusion_matrix(Y_validation, predictions))
print("\nClassification Report:\n", classification_report(Y_validation, predictions))

# Save model and scaler
joblib.dump(model, 'air_quality_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("\n✅ Model and scaler saved to disk.")
