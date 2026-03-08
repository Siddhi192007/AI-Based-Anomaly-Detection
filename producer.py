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
Producer started... Sending patient vitals
Sent: {'heart_rate': 82, 'oxygen': 96, 'bp': 118}
Sent: {'heart_rate': 90, 'oxygen': 94, 'bp': 130}
Sent: {'heart_rate': 75, 'oxygen': 97, 'bp': 110}

O
