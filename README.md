# Proyecto de Automatización de Pruebas Funcionales con Selenium y Pytest

Este proyecto fue desarrollado como parte de la evaluación del Módulo 4 de un curso de QA y Testing. El objetivo principal es demostrar la capacidad para diseñar y ejecutar una suite de automatización de pruebas funcionales utilizando para ello utilice el framework Pytest y la librería Selenium en Python.

# La suite de pruebas se enfoca en la validación de dos flujos críticos de una aplicación web:

Validación del Formulario de Registro: Pruebas para asegurar que el registro de nuevos usuarios funciona según los requisitos, incluyendo la validación de campos obligatorios, mensajes de error y reglas de negocio.

Validación del Inicio de Sesión (Login): Pruebas exhaustivas del flujo de login, cubriendo escenarios con credenciales válidas e inválidas, y simulando el comportamiento de la aplicación ante múltiples intentos fallidos.

# Tecnologías Utilizadas: 

Python: Lenguaje de programación principal.

Selenium WebDriver: Herramienta para la automatización de navegadores.

Pytest: Framework de pruebas para estructurar, organizar y ejecutar los tests.

# Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

tests/: Contiene los archivos de prueba (test_login.py, test_register.py).

utils/: Contiene scripts auxiliares, como la función para tomar capturas de pantalla (screenshots.py).

conftest.py: Archivo de configuración de Pytest para la gestión de fixtures (ej. el fixture driver para el navegador).

requirements.txt: Lista de dependencias del proyecto (selenium, pytest).

# Cómo Ejecutar las Pruebas

1- Clona este repositorio.

2- Instala las dependencias:

   pip install -r requirements.txt

3- Ejecuta los tests desde la terminal:

   pytest

4- O ejecuta un archivo de prueba específico:

   pytest tests/test_login.py

5- Puedes especificar el navegador a utilizar (Chrome es el predeterminado):

   pytest --browser firefox
