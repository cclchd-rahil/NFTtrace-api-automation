import requests

def send_request(method, url, headers=None, data=None, params=None):
    response = requests.request(
        method=method,
        url=url,
        headers=headers,
        json=data,
        params=params
    )
    return response
