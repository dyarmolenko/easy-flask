import pytest
import json


def test_healthz_success(test_connection):
    success_response = {
        "status": "Happy",
    }

    test_connection.request("GET", "/healthz")
    response = test_connection.getresponse()
    response_data = response.read()
    response_dict = json.loads(response_data.decode("utf-8"))

    assert success_response == response_dict
    assert response.status == 200
