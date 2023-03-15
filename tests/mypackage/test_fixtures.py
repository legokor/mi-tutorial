import pytest


@pytest.fixture
def users():
    return [
        {"id": 1, "name": "foo"},
        {"id": 2, "name": "bar"}
    ]

def test_users(users):
    assert users[1]["name"] == "bar"
