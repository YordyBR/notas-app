from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_login_happy_path(driver):
    driver.get("http://localhost:5000/login")
    driver.find_element(By.NAME, "usuario").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.save_screenshot('negative.png')  # <<--- Captura aquí
    assert "Bienvenido" in driver.page_source or "Notas" in driver.page_source

def test_login_negative(driver):
    driver.get("http://localhost:5000/login")
    driver.find_element(By.NAME, "usuario").send_keys("usuario_invalido")
    driver.find_element(By.NAME, "password").send_keys("mala")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.save_screenshot('negative.png')  # <<--- Captura aquí
    print(driver.page_source)  
    assert (
        "Error" in driver.page_source.lower() or
        "credenciales" in driver.page_source.lower()
    )
