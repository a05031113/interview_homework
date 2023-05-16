import pytest
from flask import Flask
from PIL import Image

from application import *


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(api)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_png(client):
    response = client.get('/api/image?width=100&height=100')

    assert response.status_code == 200
    assert response.mimetype == 'image/png'

    # Check if the image dimensions are correct
    image = Image.open(io.BytesIO(response.data))
    assert image.width == 100
    assert image.height == 100


def test_invalid_get_png(client):
    response = client.get('/api/image?width=abc&height=100')

    assert response.status_code == 500
    json_data = response.get_json()
    assert json_data is None
