import os
from datetime import datetime

def take_screenshot(driver, name):
    """
    Captura una pantalla y la guarda en una carpeta 'screenshots'
    con una marca de tiempo y un nombre específico.
    """
    # Crea la carpeta 'screenshots' si no existe
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"screenshots/{name}_{timestamp}.png"
    driver.save_screenshot(path)
    print(f"Captura de pantalla guardada en: {path}")