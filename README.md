#AI-Based Anomaly Detection System
Project Description
This project is an AI-based anomaly detection system designed to detect unusual patterns in healthcare data. The system uses machine learning to analyze patient health data and identify abnormal conditions.
#Technologies Used
- Python
- Machine Learning
- Flask
- Kafka
- Pandas
- Scikit-learn
- SQLite
- Matplotlib

#Project Structure---
AI-Anomaly-Detection
producer.py – Generates streaming healthcare data
consumer.py – Consumes data from Kafka
model.py – Machine learning anomaly detection model
database.py – Database connection and storage
api.py – Flask API backend
dashboard.py – Visualization dashboard
requirements.txt – Required libraries
README.md – Project documentation

#Workflow---
1. Data is generated using producer.py
2. Kafka streams the data in real-time
3. consumer.py processes the data
4. model.py detects anomalies using machine learning
5. Detected anomalies are stored in the database
6. Flask API sends the data to the dashboard
7. Dashboard visualizes patient health data and anomalies

#How to Run the Project
1. Install required libraries
pip install -r requirements.txt
2. Run the producer
python producer.py
3. Run the consumer
python consumer.py
4. Start the API server
5.python api.py
6. Run the dashboard
python dashboard.py
#Output==
The system detects abnormal patient health patterns and generates alerts. These anomalies can be viewed on the dashboard.

Author-----
Siddhi Chougale.
