from flask import Flask, request, jsonify
from ml_service.contribution_validity import contribution

app = Flask(__name__)


@app.route('/hello_world/', methods=['GET'])
def hello_world():  # put application's code here
    return "Let's do this...................................................................................."


@app.route('/bulkRequest', methods=['post'])
def bulk_request():
    if request.is_json:
        # Get the JSON data
        data = request.get_json()

        data = data.get('requestingAmount')

        return contribution(data)

    else:
        return jsonify({'error': 'Request must be JSON'}), 400

