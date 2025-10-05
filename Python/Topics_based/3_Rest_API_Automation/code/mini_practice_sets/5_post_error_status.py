import requests

def post_with_status(url: str, payload: dict) -> tuple[int, str]:
     resp = requests.post(url, json=payload)
     code = resp.status_code
              
     if code >=200 and code <=299:
          return (code, "OK")
     else:
          return (code, "FAIL")

if __name__=="__main__":
     print(post_with_status("https://httpbin.org/status/404", payload = {"name": "babu", "role": "devops"}))         
