import requests
import json

url = {
"terminalwait":"https://avi-prod-mpp-webapp-api.azurewebsites.net/api/v1/TaxiWaitTimePoints/JFK",
"gatewalk":"https://avi-prod-mpp-webapp-api.azurewebsites.net/api/v1/SecurityWaitTimesPoints/JFK",
"immigration":"https://avi-prod-mpp-webapp-api.azurewebsites.net/api/v1/SecurityWaitTimesPoints/JFK"
}
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:147.0) Gecko/20100101 Firefox/147.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.jfkairport.com/',
    'Origin': 'https://www.jfkairport.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}

response1 = requests.request("GET", url["terminalwait"], headers=headers)
response2 = requests.request("GET", url["gatewalk"], headers=headers)
response3 = requests.request("GET", url["immigration"], headers=headers)


print(json.dumps(response1.json(), indent=2))
print("-------------------------------------------------------------------------------------------------------------")
print(json.dumps(response2.json(), indent=2))
print("-------------------------------------------------------------------------------------------------------------")
print(json.dumps(response3.json(), indent=2))
