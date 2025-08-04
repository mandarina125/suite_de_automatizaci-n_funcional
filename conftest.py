
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use for tests")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
