import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    yield driver
    driver.quit()

@pytest.mark.smoke
def test_page_title(driver):
    driver.get("https://jsonplaceholder.typicode.com")
    assert "JSONPlaceholder" in driver.title

@pytest.mark.smoke
def test_page_loads(driver):
    driver.get("https://jsonplaceholder.typicode.com")
    assert driver.current_url == "https://jsonplaceholder.typicode.com/"

@pytest.mark.regression
def test_heading_exists(driver):
    driver.get("https://jsonplaceholder.typicode.com")
    heading = driver.find_element(By.TAG_NAME, "h1")
    assert heading is not None