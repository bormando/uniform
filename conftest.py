import pytest
import time


# noinspection SpellCheckingInspection
def pytest_addoption(parser):
    parser.addoption("--timeout", action="store", default="3", help="Timeout delay between tests")


@pytest.fixture(autouse=True, scope="function")
def timeout(request):
    timeout_delay = int(request.config.getoption("timeout"))
    yield time.sleep(timeout_delay)
