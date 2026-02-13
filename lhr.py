import requests
import json
url = {
    "security":"https://api-dp-prod.dp.heathrow.com/pihub/immigrationwaittime/ByTerminal/2"
}
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:147.0) Gecko/20100101 Firefox/147.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.heathrow.com/',
    'Origin': 'https://www.heathrow.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Connection': 'keep-alive',
}
response1 = requests.request("GET", url["security"], headers=headers)
print(json.dumps(response1.json(), indent=2))
print("-----------------------------------------------------------------------------------------")
