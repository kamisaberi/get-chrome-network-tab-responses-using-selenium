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

f1 = open("logs.txt", "wt")
sys.stdout = f1

options = Options()
options.set_capability('goog:loggingPrefs', {'performance': 'ALL', "browser": "ALL", 'driver': 'ALL'})
# options.add_argument("--headless")  # Optional: run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)


def processLog(log):
    log = json.loads(log["message"])["message"]
    # print("-----------------------")
    # print(log["method"])
    # print("\n")
    # if ("Network.response" in log["method"] and "params" in log.keys()):
    if ("Network.response" in log["method"] and "params" in log.keys()):
        # print(log["method"])
        # headers = log["params"]["response"]
        try:
            print("-----------------------------------------------------------")
            print(log["params"]["requestId"],log["params"]["type"] if "type" in log["params"] else "None")
            # print("Req Id:", log["params"]["requestId"])
            body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': log["params"]["requestId"]})
            # print(json.dumps(body, indent=4, sort_keys=True))
            # log['body'] = json.dumps(body, indent=4, sort_keys=True)
            log['body'] = body
        except WebDriverException:
            print(log["params"]["requestId"], log["params"]["type"] if "type" in log["params"] else "None")
            print('response.body is null')
        # except JSONDecodeError:
        #     print('response.body is not json')
    # elif ("Network.requestWillBeSent" == log["method"]):
    #     print("script")
    #     body = driver.execute_script(log["params"]["request"]["url"], {'requestId': log["params"]["requestId"]})
    #     print(body)

    # print("-----------------------")
    return log


# url = "https://www.nike.com/ie/t/jordan-essentials-puffer-jacket-KgsFWB/FB7311-340"
url = "https://www.asos.com/asos-design/asos-design-muscle-fit-long-sleeve-rib-polo-in-navy/prd/207188815"
file_name = url.split("/")[-1] + ".json"
driver.get(url)
time.sleep(10)
logs = driver.get_log('performance')
responses = []
for log in logs:
    responses.append(processLog(log))

print(len(responses))
time.sleep(2)
# for response in responses:
#
#     print(response)


with open(file_name, "wt") as f:
    f.write(json.dumps(responses))
# print(responses)

time.sleep(20)
