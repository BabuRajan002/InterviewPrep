from pathlib import Path
import re
from collections import Counter

def top_paths(path: str, k: int=3) -> list[tuple[str, int]]:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(file_path)
    with file_path.open('r', encoding='utf-8') as f:
        endpoints = []
        methods = ['GET', 'POST', 'PUT', 'DELETE']
        for line in f:
            line = line.strip()
            for method in methods:
                if line.__contains__(method):
                   pattern = rf"\b{method}\s+(\S+)"
                   match = re.search(pattern, line)
                   if match:
                       endpoint = match.group(1).split("?")[0]
                       endpoints.append(endpoint)
        endpoint_count = Counter(endpoints)
        top_endpoints = endpoint_count.most_common(k)
        return top_endpoints 
if __name__ == "__main__":
    top_path_counts = top_paths("/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/1_Basics_Foundation/sample_files/access.log", 3)
    for top_path_count in top_path_counts:
        print(f"{top_path_count[0]} {top_path_count[1]}")

# # ChatGPT Version
# from pathlib import Path
# from collections import Counter
# import re
# from typing import List, Tuple

# def top_paths(path: str, k: int = 3) -> List[Tuple[str, int]]:
#     """Return top-k endpoints from access.log, ignoring query strings."""
#     file_path = Path(path)
#     if not file_path.exists():
#         raise FileNotFoundError(file_path)

#     endpoints = []
#     with file_path.open("r", encoding="utf-8") as f:
#         for line in f:
#             match = re.search(r'"(GET|POST|PUT|DELETE)\s+(\S+)', line)
#             if not match:
#                 continue
#             endpoint = match.group(2).split("?")[0]
#             endpoints.append(endpoint)

#     counts = Counter(endpoints)
#     # Sort by count desc, then path asc
#     return sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:k]

# if __name__ == "__main__":
#     for path, count in top_paths("access.log", 3):
#         print(f"{path} {count}")

    

