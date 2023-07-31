from server import app
import pytest
import json


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
