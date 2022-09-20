import pprint

import requests

resp = requests.get("https://api.spacexdata.com/v3/history")

print(resp.status_code)
print(resp.text)
pprint.pprint(resp.json())