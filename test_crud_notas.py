import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def test_crear_nota_happy_path(driver):
    driver.get("http://localhost:5000/nueva_nota")
    driver.find_element(By.NAME, "titulo").send_keys("Título de prueba")
    driver.find_element(By.NAME, "contenido").send_keys("Texto de prueba para la nota")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.save_screenshot('happy_path.png')  # <<--- Captura aquí
    assert "Notas" in driver.page_source  
    
@pytest.fixture
def test_crear_nota_negative(driver):
    driver.get("http://localhost:5000/nueva_nota")
    driver.find_element(By.NAME, "titulo").send_keys("Título de prueba")
    driver.find_element(By.NAME, "contenido").clear()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.save_screenshot('negative.png')  # <<--- Captura aquí
    assert "obligatorio" in driver.page_source or "error" in driver.page_source