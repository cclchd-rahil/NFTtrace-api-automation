import pytest
from utils.api_requests import send_request
from utils.token_manager import get_auth_token
from configs.config import CONFIG

@pytest.mark.smoke
def test_get_users(env):
    base_url = CONFIG[env]["base_url"]

    # 🔥 Get dynamic token
    token = get_auth_token(env)

    # Prepare headers with dynamic token
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    endpoint = "/api/v1/organization-user-roles"

    response = send_request(
        method="GET",
        url=base_url + endpoint,
        headers=headers
    )

    print("Response:", response.json())

    assert response.status_code == 200
    assert "users" in response.json()
