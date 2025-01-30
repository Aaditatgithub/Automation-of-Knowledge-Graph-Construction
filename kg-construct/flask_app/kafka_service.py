from kafka import KafkaProducer
from config import Config
import json

# Kafka Configuration
KAFKA_BROKER = Config.KAFKA_BROKER  # Update if using a remote Kafka broker
TOPIC_NAME = Config.TOPIC_NAME

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize JSON data
)

def send_response_to_kafka(row):
    """
    Send data to Kafka topic.
    """
    try:
        producer.send(TOPIC_NAME, row)
        producer.flush()  # Ensure the message is sent immediately
        # print(f"Data sent to Kafka topic: {TOPIC_NAME}")
        return {'status': 'success', 'message': 'Data sent to Kafka'}
    except Exception as e:
        # print(f"Error sending to Kafka: {str(e)}")
        return {'status': 'error', 'message': str(e)}
