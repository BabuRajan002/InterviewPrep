import requests

def safe_get(url: str, **kwargs):
    try:
        r = requests.get(url, timeout=10, **kwargs)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

print(safe_get("https://httpbin.org/"))