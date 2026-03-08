The File reads data and checks for  anomalies:

from database import get_data
from model import detect_anomaly

data = get_data()

for value in data:
    result = detect_anomaly(value)
    print("Value:", value, "Status:", result)
Output:
Value: 45 Status: Normal
Value: 95 Status: Anomaly
