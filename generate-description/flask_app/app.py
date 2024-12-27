from flask import Flask, request, jsonify
from flask_cors import CORS
from kafka import KafkaProducer
import json

# Initialize Flask app
app = Flask(__name__)

# Enable CORS to allow React to communicate with Flask
CORS(app)

# Kafka Configuration
KAFKA_BROKER = 'localhost:9092'  # Update if using a remote Kafka broker
TOPIC_NAME = 'test_topic'

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize JSON data
)

@app.route('/send', methods=['POST'])
def send_to_kafka():
    """
    Endpoint to send a single row to Kafka.
    Expects JSON payload with the row data.
    """
    try:
        # Get the JSON data from the request
        row = request.json

        if not row:
            return jsonify({'status': 'error', 'message': 'No data provided'}), 400

        # Send the row to Kafka
        producer.send(TOPIC_NAME, row)
        producer.flush()  # Ensure the message is sent immediately

        return jsonify({'status': 'success', 'message': 'Row sent to Kafka'}), 200

    except Exception as e:
        # Handle errors
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, port=5000)
