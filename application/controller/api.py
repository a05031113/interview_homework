from flask import *
from PIL import Image
from dotenv import load_dotenv
import os
import io
import uuid
import requests
load_dotenv()


api = Blueprint('api', __name__)


@api.route('/api/image', methods=['GET'])
def get_png():
    try:
        track_api_execution()

        width = int(request.args.get('width'))
        height = int(request.args.get('height'))

        image = Image.new('RGB', (width, height))
        filename = io.BytesIO()
        image.save(filename, format="PNG")
        filename.seek(0)
        return send_file(filename, mimetype='image/png')
    except:
        return jsonify({"error": True, "message": SyntaxError}), 500


def track_api_execution():
    api_secret = os.getenv("api_secret")
    measurement_id = "G-CRTZZ2HL4S"
    url = 'https://www.google-analytics.com/mp/collect?measurement_id=' + \
        api_secret+'&api_secret='+measurement_id

    payload = {
        'client_id': uuid.uuid4(),
        'events': [{
            'name': 'qsearch',
            'params': {}
        }]
    }
    headers = {'content-type': 'application/json'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code != 200:
        print('Failed to send API execution data to Google Analytics.')
