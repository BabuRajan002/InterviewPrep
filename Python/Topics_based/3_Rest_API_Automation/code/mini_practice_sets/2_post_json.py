import requests


def post_echo(url: str, payload): 
    try:
        resp = requests.post(url, json=payload)
        resp.raise_for_status()
        if resp.headers.get('Content-Type', '').startswith("application/json"):
          return resp.json()['json'], resp.url
        return None
    except requests.exceptions.RequestException as e:
        print(f"HTTP error {e}")
        return None

if __name__ == "__main__":
   print(post_echo("https://httpbin.org/post", payload = {"name": "babu", "role": "devops"}))