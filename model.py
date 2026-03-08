from sklearn.ensemble import IsolationForest
import numpy as np

model = IsolationForest(contamination=0.1)

train_data = np.array([
[70,98,36.5],
[75,97,36.6],
[80,96,36.7],
[72,99,36.4]
])

model.fit(train_data)

def detect_anomaly(vitals):

    data = [[
    vitals["heart_rate"],
    vitals["oxygen"],
    vitals["temperature"]
    ]]

    result = model.predict(data)

    score = int(result[0])

    if score == -1:
        severity = "HIGH"
    else:
        severity = "LOW"

    return score, severity

Output:
vitals = {
    "patient_id": 2,
    "heart_rate": 120,
    "oxygen": 95,
    "temperature": 37.8
}
Security:MEDIUM


O
