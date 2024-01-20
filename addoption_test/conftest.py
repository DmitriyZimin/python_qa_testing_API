import pytest


def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru", help="Yandex API URL")
    parser.addoption("--status_code", default=200, type=int, help="Response status code")


@pytest.fixture
def ya_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def ya_status_code(request):
    return request.config.getoption("--status_code")
