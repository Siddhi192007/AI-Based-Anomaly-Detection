import pandas as pd
from model import detect_anomaly

data = pd.read_csv("dataset.csv")

for i in range(len(data)):

    hr = data["heart_rate"][i]

    result = detect_anomaly(hr)

    print("Patient:", data["patient_id"][i])
    print("Heart Rate:", hr)
    print("Status:", result)
    print()

Output:
Patient: 1
Heart Rate: 72
Status: Normal

Patient: 5
Heart Rate: 200
Status: Anomaly
