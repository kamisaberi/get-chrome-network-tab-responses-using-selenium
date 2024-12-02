import threading
import time
import json
from json import JSONDecodeError

from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import sys

import defs

f1 = open("logs.txt", "wt")
sys.stdout = f1

driver = defs.create_driver()

def process_log(log):
    log = json.loads(log["message"])["message"]
    if ("Network.response" in log["method"] and "params" in log.keys()):
        try:
            print("-----------------------------------------------------------")
            print(log["params"]["requestId"], log["params"]["type"] if "type" in log["params"] else "None")
            body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': log["params"]["requestId"]})
            log['body'] = body
        except WebDriverException:
            print(log["params"]["requestId"], log["params"]["type"] if "type" in log["params"] else "None")
            print('response.body is null')
    return log


url = "https://www.asos.com/asos-design/asos-design-muscle-fit-long-sleeve-rib-polo-in-navy/prd/207188815"
file_name = url.split("/")[-1] + ".json"
driver.get(url)
time.sleep(10)
logs = driver.get_log('performance')
responses = []
for log in logs:
    responses.append(process_log(log))

print(len(responses))
time.sleep(2)
# for response in responses:
#
#     print(response)


with open(file_name, "wt") as f:
    f.write(json.dumps(responses))
# print(responses)

time.sleep(20)
