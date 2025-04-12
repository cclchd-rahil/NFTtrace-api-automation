import pytest

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev")

@pytest.fixture
def env(request):
    return request.config.getoption("--env")

@pytest.fixture
def base_url(env):
    if env == "dev":
        return "https://api-dev-psql.murundi.nfttrace.com"
    elif env == "live":
        return "https://api-dev-psql.murundi.nfttrace.com"
