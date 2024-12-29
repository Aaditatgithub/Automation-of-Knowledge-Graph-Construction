from flask import Flask, request, jsonify
from flask_cors import CORS
from kafka import KafkaProducer
import requests
import json

# Initialize Flask app
app = Flask(__name__)

# Enable CORS to allow React to communicate with Flask
CORS(app)

# Kafka Configuration
KAFKA_BROKER = 'localhost:9092'  # Update if using a remote Kafka broker
TOPIC_NAME = 'test_topic'

# Groq API Configuration
GROQ_API_KEY = "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"
GROQ_API_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize JSON data
)

def call_groq_api(row):
    """
    Call the Groq API with the received Kafka message and get a structured response.
    Combine all fields into a single text and use feature_image for the image_url.
    """
    # Combine all fields into a single text
    combined_text = "\n".join([f"{key}: {value}" for key, value in row.items() if key != "feature_image"])

    payload = {
        "model": "llama-3.2-11b-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": combined_text
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": row.get("feature_image", "")
                        }
                    }
                ]
            }
        ],
        "temperature": 1,
        "max_tokens": 1024,
        "top_p": 1,
        "stream": False,
        "stop": None
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(GROQ_API_ENDPOINT, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        result = response.json()
        print("Groq API Response (Structured):", json.dumps(result, indent=2))
        return result.get("choices", [{}])[0].get("message", "No message returned.")
    else:
        error_message = {"error": f"Error: {response.status_code} - {response.text}"}
        print("Groq API Error Response:", error_message)
        return error_message

@app.route('/send', methods=['POST'])
def send_to_kafka():
    """
    Endpoint to send a single row to Kafka and process with Groq API.
    Expects JSON payload with the row data.
    """
    try:
        # Get the JSON data from the request
        row = request.json

        if not row:
            return jsonify({'status': 'error', 'message': 'No data provided'}), 400

        # Print the received object
        # print("Received object:", json.dumps(row, indent=2))

        # Call Groq API and get the structured response
        groq_response = call_groq_api(row)
        print("Final Groq API Response for the Flask Console:", json.dumps(groq_response, indent=2))

        # Send the row to Kafka
        producer.send(TOPIC_NAME, row)
        producer.flush()  # Ensure the message is sent immediately

        return jsonify({'status': 'success', 'message': 'Row sent to Kafka', 'groq_response': groq_response}), 200

    except Exception as e:
        # Handle errors
        print("Error occurred:", str(e))
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, port=5000)
