import requests

def handle_non_json(url: str):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        if resp.headers.get("Content-Type", "").startswith("text/html"):
            return resp.text[:120]
        return "No HTML content"
    except requests.exceptions.RequestException as e:
        print(f"http error {e}")
        return None

if __name__ == "__main__":
    print(handle_non_json("https://httpbin.org/html"))


#ChatGPT version
# import requests

# def handle_non_json(url: str, length: int = 120) -> str:
#     try:
#         resp = requests.get(url, timeout=5)
#         resp.raise_for_status()
#         if resp.headers.get("Content-Type", "").startswith("text/html"):
#             return resp.text[:length]
#         return "Not HTML content"
#     except requests.exceptions.RequestException as e:
#         print("HTTP error:", e)
#         return "Request failed"

# if __name__ == "__main__":
#     print(handle_non_json("https://httpbin.org/html"))
