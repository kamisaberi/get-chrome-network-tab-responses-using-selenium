from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json

# from seleniumwire.undetected_chromedriver import ChromeOptions

# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Optional: run in headless mode
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

options = Options()
options.set_capability('goog:loggingPrefs', {'performance': 'ALL', "browser": "ALL", 'driver': 'ALL'})
# options.add_argument("--headless")  # Optional: run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get("https://www.nike.com/ie/w/mens-clothing-6ymx6znik1")
logs = driver.get_log('performance')
data = []
for entry in logs:
    log = json.loads(entry['message'])['message']
    # log = json.loads(entry['message'])
    # print(type(entry))
    # log = json.loads(entry)
    # data.append(entry)
    if 'Network.responseReceived' in log.get('method', ''):
        pass
        # print(log)
    # response_url = log['params']['response']['url']
    response_url = log['params']
    print(response_url)
    if "makemytrip" in response_url:
        print("Url:", response_url)
        # print("Response headers:", log['params']['response']['headers'])
        print("Response headers:", log['params'])

time.sleep(20)

# Clean up
# with open('nike2.json', 'w') as outfile:
#     outfile.write(json.dumps(data))
driver.quit()

time.sleep(20)
