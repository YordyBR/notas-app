from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_chrome():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()


USERNAME = "admin"
PASSWORD = "admin123"

def test_chrome():
    driver = None
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.google.com")
        assert "Google" in driver.title
    finally:
        if driver:
            driver.quit()