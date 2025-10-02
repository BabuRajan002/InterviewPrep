import requests

headers = {"Authorization": "Bearer FAKE-TOKEN", "Accept": "application/json"}

resp = requests.get("https://httpbin.org/headers", headers=headers)
print(resp.json()["headers"])