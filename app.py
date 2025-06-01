from flask import Flask, request, jsonify
from ml_service.contribution_validity_service import contribution
from utils.random_data.create_data import generate_random_sample_data

app = Flask(__name__)

@app.route('/generateSamples', methods=['post'])
def generate_samples():
    try:
        generate_random_sample_data()
        return jsonify({'res':'New samples generated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/bulkRequest', methods=['post'])
def bulk_request():

    response = None
    if request.is_json:
        # Get the JSON data
        data = request.get_json()

        expecting_item = data.get('itemId')
        expecting_amount = data.get('requestingAmount')

        try:
            response = contribution(int(expecting_item), expecting_amount)
            return response
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    else:
        return jsonify({'error': 'Request must be JSON'}), 400

