import requests

def send_bearer(url: str, token):
    try:
        resp = requests.get(url, headers=token)
        resp.raise_for_status()
        if resp.headers.get("Content-Type").startswith("application/json"):
            return resp.json()['headers']['Authorization']
    except requests.exceptions.RequestException as e:
        print(f"HTTP error {e}")
        return None

if __name__ == "__main__":
    echoed = send_bearer("https://httpbin.org/headers", {"Authorization": "Bearer FAKE-TOKEN-123"})
    print(f"echoed token from the url {echoed}")