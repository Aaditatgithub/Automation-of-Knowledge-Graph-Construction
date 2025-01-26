from flask import Flask, request, jsonify
from flask_cors import CORS
from kafka_service import send_response_to_kafka
from classification_service import classify_product
from feature_extraction import get_structured_output
import json

# Initialize Flask app
app = Flask(__name__)

# Enable CORS to allow React to communicate with Flask
CORS(app)

@app.route('/send', methods=['POST'])
def get_data_from_kafka():
    """
    Endpoint to send response of data ingestion to Kafka.
    Expects JSON payload with the row data.
    """
    try:
        # Step 1: Get the JSON data from the request
        product_data = request.json
        if not product_data:
            return jsonify({'status': 'error', 'message': 'No data provided'}), 400
        # print(product_data)

        # Step 2: Extract only the product name
        product_name = product_data["product_name"]

        # Step 3: Call the classification function with only the product name
        product_class = classify_product({"name": product_name})
        print("Product class:" + product_class)

        # Step 4: Get structured output from LLM
        taxonomical_class = get_structured_output(product_data, product_class)
        print(taxonomical_class)

        # Step 5: Execute CypherSQL query


        return jsonify({
            'status': 'success',
            'message': 'Node accomodated in graph',
        }), 200
    
    except Exception as e:
        # Handle errors
        print("Error occurred:", str(e))
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, port=5000)
