import pytest
from http import client

@pytest.fixture
def test_connection() -> client.HTTPConnection:
    connection = client.HTTPConnection("127.0.0.1", 5000)
    return connection
    