import requests

params = {"q": "devops", "limit": 3}

resp = requests.get("https://httpbin.org/get", params=params)

print(resp.url)
print(resp.json()["args"])