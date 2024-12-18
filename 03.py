import json
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json

options = Options()
options.set_capability('goog:loggingPrefs', {'performance': 'ALL', "browser": "ALL", 'driver': 'ALL'})
# options.add_argument("--headless")  # Optional: run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)


def processLog(log):
    log = json.loads(log["message"])["message"]
    if ("Network.response" in log["method"] and "params" in log.keys()):
        # headers = log["params"]["response"]
        try:
            body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': log["params"]["requestId"]})
            log['body'] = body
            print(json.dumps(body, indent=4, sort_keys=True))
        except WebDriverException:
            print('response.body is null')
    return log["params"]


driver.get("https://www.nike.com/ie/w/mens-clothing-6ymx6znik1")
logs = driver.get_log('performance')
responses = [processLog(log) for log in logs]
print(responses)
time.sleep(20)