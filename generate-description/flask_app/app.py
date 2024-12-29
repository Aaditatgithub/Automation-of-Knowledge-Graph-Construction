from flask import Flask, request, jsonify
from flask_cors import CORS
from kafka_service import send_to_kafka
from groq_service import call_groq_api
import json

# Initialize Flask app
app = Flask(__name__)

# Enable CORS to allow React to communicate with Flask
CORS(app)

@app.route('/send', methods=['POST'])
def send_to_kafka_endpoint():
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
        # print("Final Groq API Response for the Flask Console:", json.dumps(groq_response, indent=2))

        # Send the row to Kafka
        kafka_response = send_to_kafka(row)

        return jsonify({
            'status': 'success',
            'message': 'Row sent to Kafka',
            'kafka_response': kafka_response,
            'groq_response': groq_response
        }), 200

    except Exception as e:
        # Handle errors
        print("Error occurred:", str(e))
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, port=5000)
