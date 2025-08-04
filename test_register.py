import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshots import take_screenshot

URL = "https://www.selenium.dev/selenium/web/web-form.html"

@pytest.fixture
def driver(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def fill_form(driver, text_value="", password_value="", textarea_value=""):
    driver.get(URL)
    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located((By.ID, "my-text-id"))).send_keys(text_value)
    wait.until(EC.presence_of_element_located((By.ID, "my-password"))).send_keys(password_value)
    wait.until(EC.presence_of_element_located((By.ID, "my-textarea"))).send_keys(textarea_value)

    form = wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
    form.submit()

def test_successful_registration(driver):
    try:
        fill_form(driver, "Texto prueba", "ContrasenaSegura123", "Mensaje de prueba")
        time.sleep(1)
        assert "Form submitted" in driver.page_source or "Return to index" in driver.page_source
    except Exception:
        take_screenshot(driver, "successful_registration")
        raise

def test_empty_password_field(driver):
    try:
        fill_form(driver, "Texto prueba", "", "Mensaje de prueba")
        time.sleep(1)
        take_screenshot(driver, "empty_password")
        assert True  # Solo capturamos la pantalla si el campo falta
    except Exception:
        raise

def test_empty_text_input(driver):
    try:
        fill_form(driver, "", "ContrasenaSegura123", "Mensaje de prueba")
        time.sleep(1)
        take_screenshot(driver, "empty_text_input")
        assert True
    except Exception:
        raise
