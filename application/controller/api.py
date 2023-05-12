from flask import *
from PIL import Image
import io

api = Blueprint('api', __name__)


@api.route('/api/image', methods=['GET'])
def get_png():
    try:
        width = int(request.args.get('width'))
        height = int(request.args.get('height'))

        image = Image.new('RGB', (width, height))
        filename = io.BytesIO()
        image.save(filename, format="PNG")
        filename.seek(0)
        return send_file(filename, mimetype='image/png')
    except:
        return jsonify({"error": True, "message": SyntaxError}), 500
