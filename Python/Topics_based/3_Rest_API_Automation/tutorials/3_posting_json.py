import requests

data = {"name": "babu", "role": "devops"}

resp = requests.post("https://httpbin.org/get", json=data)
print(resp.status_code)
print(resp.headers["Content-Type"]) #Data text/html format