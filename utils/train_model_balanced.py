import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Load and merge
sensor = pd.read_csv("sensor_data.csv")
quality = pd.read_csv("quality_control_data.csv")
data = sensor.merge(quality, on="prod_id").drop(columns='prod_id')

# Separate classes
good = data[data['quality'] == 'good']
poor = data[data['quality'] == 'poor']

good_sampled = good.sample(n=len(poor), random_state=42)
balanced_data = pd.concat([good_sampled, poor], axis=0)

balanced_data = balanced_data.sample(frac=1, random_state=42)

X = balanced_data[['weight', 'humidity', 'temperature']]
y = balanced_data['quality']

# Encode target (good = 1, poor = 0)
y = y.map({'good': 1, 'poor': 0})

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Training this model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print("Report:\n", classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "air_quality_model.pkl")
