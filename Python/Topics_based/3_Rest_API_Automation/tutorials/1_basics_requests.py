import requests

#Simple GET

resp = requests.get("https://httpbin.org/get")
print(resp.status_code)
print(resp.json())