import pandas as pd

sensor = pd.read_csv("sensor_data.csv")
quality = pd.read_csv("quality_control_data.csv")
merged = sensor.merge(quality, on="prod_id")

print("Class distribution:\n", merged['quality'].value_counts())
