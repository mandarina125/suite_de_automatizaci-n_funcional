import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshots import take_screenshot

# URL de la página de inicio de sesión de Heroku App
LOGIN_URL = "https://the-internet.herokuapp.com/login"


USERS_DATA = {
    "valid_user": {"username": "tomsmith", "password": "SuperSecretPassword!"},
    "invalid_user_pass": {"username": "tomsmith", "password": "wrongpassword"},
    "invalid_user_name": {"username": "invaliduser", "password": "SuperSecretPassword!"},
    "invalid_both": {"username": "invaliduser", "password": "wrongpassword"}
}

def login(driver, username, password):
    """
    Función auxiliar para realizar el proceso de login en Heroku App.
    """
    driver.get(LOGIN_URL)
    wait = WebDriverWait(driver, 10)

    # Esperar y encontrar los campos de usuario y contraseña y el botón de login
    username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
    
    username_field.send_keys(username)
    password_field.send_keys(password)

    
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".fa.fa-2x.fa-sign-in")))
    login_button.click()
    time.sleep(1) 

def test_successful_login(driver):
    """
    Escenario: Inicio de sesión exitoso con credenciales válidas en Heroku App.
    """
    try:
        user_data = USERS_DATA["valid_user"]
        login(driver, user_data["username"], user_data["password"])
        
        # Verificar que el login fue exitoso.
        
        wait = WebDriverWait(driver, 10)
        success_message = wait.until(EC.presence_of_element_located((By.ID, "flash")))
        
        assert "You logged into a secure area!" in success_message.text
        assert "secure" in driver.current_url
        print(f"Login exitoso para {user_data['username']}")
        take_screenshot(driver, "Login exitoso")
        
    except Exception as e:
        take_screenshot(driver, "successful_login_failure")
        pytest.fail(f"Fallo en el login exitoso: {e}")

@pytest.mark.parametrize("test_case", ["invalid_user_pass", "invalid_user_name", "invalid_both"])
def test_invalid_credentials_login(driver, test_case):
    """
    Escenario: Inicio de sesión fallido con credenciales inválidas en Heroku App.
    La página muestra un mensaje de error y permanece en la URL de login.
    """
    try:
        user_data = USERS_DATA[test_case]
        login(driver, user_data["username"], user_data["password"])
        
        # Verificar que el login falló.
        
        wait = WebDriverWait(driver, 10)
        error_message = wait.until(EC.presence_of_element_located((By.ID, "flash")))
        
        assert "Your username is invalid!" in error_message.text or "Your password is invalid!" in error_message.text
        assert "login" in driver.current_url
        print(f"Login fallido esperado para {user_data['username']} ({test_case})")
        take_screenshot(driver, f"invalid_credentials_login_success_{test_case}") # Se toma screenshot porque es el comportamiento esperado
    except Exception as e:
        take_screenshot(driver, f"invalid_credentials_login_failure_{test_case}")
        pytest.fail(f"Fallo en la prueba de credenciales inválidas ({test_case}): {e}")

@pytest.mark.parametrize("attempt", range(4)) # Por ejemplo, 3 intentos fallidos y el 4to para el "bloqueo"
def test_account_lockout_behavior_simulated(driver, attempt):
    
    try:
        # credenciales inválidas repetidamente para simular intentos de bloqueo
        user_data = USERS_DATA["invalid_user_pass"]
        print(f"Intento {attempt + 1} de login para simular bloqueo: {user_data['username']}")
        login(driver, user_data["username"], user_data["password"])

        wait = WebDriverWait(driver, 10)
        error_message = wait.until(EC.presence_of_element_located((By.ID, "flash")))

        # En Heroku, el mensaje de error sigue siendo el mismo, no hay un mensaje de "cuenta bloqueada"
        assert "Your username is invalid!" in error_message.text or "Your password is invalid!" in error_message.text
        assert "login" in driver.current_url
        print(f"Mensaje de error persistente en intento {attempt + 1}")
        
        take_screenshot(driver, f"simulated_lockout_attempt_{attempt + 1}")

    except Exception as e:
        take_screenshot(driver, f"simulated_lockout_failure_attempt_{attempt + 1}")
        pytest.fail(f"Fallo en la simulación de bloqueo de cuenta en el intento {attempt + 1}: {e}")
