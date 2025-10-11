import requests
from typing import List

def fetch_titles(url: str, pages: int, limit: int = 10) -> List[str]:
  try:  
    resp = requests.get(url, params={"_page": pages, "_limit": limit})
    code = resp.status_code
    if code >=200 and code <=299:
      if resp.headers.get("Content-Type", "").startswith("application/json"):
        resp_lst = resp.json()
        title: List[str] = []
        for i in range(0, len(resp_lst), 1):
           title.append(resp_lst[i]["title"])
      return title
    else:
       print(f"Page is not loading {code}")
  except requests.exceptions.RequestException as e:
       print(f"HTTP Error {e}")

if __name__ == "__main__":
    print(fetch_titles("https://jsonplaceholder.typicode.com/posts", 10))
   