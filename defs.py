from selenium.common import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def create_driver():
    options = Options()
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL', "browser": "ALL", 'driver': 'ALL'})
    # options.add_argument("--headless")  # Optional: run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    return driver
