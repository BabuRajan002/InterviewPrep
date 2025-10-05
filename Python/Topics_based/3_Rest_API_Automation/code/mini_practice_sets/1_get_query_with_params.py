import requests

def get_query_params(url: str, **kwargs):
    try: 
        resp = requests.get(url, **kwargs)
        resp.raise_for_status()
        if resp.headers.get("Content-Type", "").startswith("application/json"):
            return resp.json()["args"], resp.url
    except requests.exceptions.RequestException as e:
        print(f"HTTP error {e}")
        return None, resp
    

print(get_query_params("https://httpbin.org/get", params={"q":"devops","limit":3}))