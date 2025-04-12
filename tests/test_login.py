import pytest
from utils.api_requests import send_request

@pytest.mark.smoke
def test_login_success(base_url):
    url = f"{base_url}//api/v1/auth/login"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "email":"host@nfttrace.com",
        "password":"admin@123"
    }

    response = send_request("POST", url, headers=headers, data=payload)

    assert response.status_code == 200
    assert "token" in response.json()
