from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        "heart_rate": random.randint(60,120),
        "oxygen": random.randint(85,100),
        "bp": random.randint(90,140)
    }

    producer.send('patient_data', data)
    print("Sent:", data)
    time.sleep(2)

Output:

Producer Started

Sent: {'patient_id': 1, 'heart_rate': 78, 'oxygen': 98, 'temperature': 36.6}

Sent: {'patient_id': 2, 'heart_rate': 115, 'oxygen': 95, 'temperature': 37.9}

Sent: {'patient_id': 3, 'heart_rate': 70, 'oxygen': 99, 'temperature': 36.4}

Sent: {'patient_id': 4, 'heart_rate': 130, 'oxygen': 93, 'temperature': 38.5}
