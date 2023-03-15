import pytest
import requests

# Mark test for filtering
@pytest.mark.network_access
@pytest.mark.xfail
def test_network():
    x = requests.get('https://w3schools.com')
    assert x.status_code == 200
