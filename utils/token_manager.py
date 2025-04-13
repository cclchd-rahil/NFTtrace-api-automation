from utils.api_requests import send_request
from configs.config import CONFIG

def get_auth_token(env):
    base_url = CONFIG[env]["base_url"]
    login_endpoint = "/api/v1/auth/login"  # 🔥 your login endpoint
    login_payload = {
        "email": CONFIG[env]["email"],
        "password": CONFIG[env]["password"]
    }

    response = send_request(
        method="POST",
        url=base_url + login_endpoint,
        data=login_payload
    )

    assert response.status_code == 200, "Login failed!"
    token = response.json().get("token")  # ✅ Use the correct key based on your API response

    return token
