import pytest
import requests

@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    """Disables network call through the requests module's get method."""
    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())
