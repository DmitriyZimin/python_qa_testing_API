import pytest


def pytest_addoption(parser):
    parser.addoption("--url", default="https://jsonplaceholder.typicode.com/posts", help="Jsonplaceholder API URL")


@pytest.fixture(scope='session')
def jsonplaceholder_api_base_url(request):
    return request.config.getoption("--url")
