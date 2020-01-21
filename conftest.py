import pytest
import time


# noinspection SpellCheckingInspection
def pytest_addoption(parser):
    parser.addoption("--timeout", action="store", default="3", help="Timeout delay between tests")


# It's better to use timeout between tests to not "bomb" market's API with our requests
@pytest.fixture(autouse=True, scope="function")
def timeout(request):
    timeout_delay = int(request.config.getoption("timeout"))
    yield time.sleep(timeout_delay)
