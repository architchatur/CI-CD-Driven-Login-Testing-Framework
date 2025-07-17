from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

URL = "http://the-internet.herokuapp.com/login"

@pytest.fixture
def driver():
    # Set up headless Chrome for CI
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Automatically download and manage ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

# ✅ Smoke Test: Does the login page load?
def test_login_page_loads(driver):
    driver.get(URL)
    assert "The Internet" in driver.title

# ✅ Integration Test: Successful login
def test_login_success(driver):
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()
    message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in message

# ✅ Sanity Test: Login failure with wrong credentials
def test_login_failure(driver):
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("wrong")
    driver.find_element(By.ID, "password").send_keys("wrong")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()
    message = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in message
