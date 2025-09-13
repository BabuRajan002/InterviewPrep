from pathlib import Path
def extract_error_codes(path: str) -> list[str]:
    file_path = Path(path)
    if not file_path.exists():
       raise FileNotFoundError(file_path)

    with file_path.open('r', encoding="utf-8") as error_file: 
        error_codes = []
        for line in error_file:
             line = line.strip()
             if line.__contains__('ERROR'):
                 code = line.split('=')
                 error_code = code[1].split(" ")
                 error_codes.append(error_code[0])        
        lst = sorted(list(set(error_codes)))
        return f"ERROR codes: {",".join(lst)}"

if __name__ == "__main__":
    print(extract_error_codes("/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/1_Basics_Foundation/sample_files/distinct_error_code.log"))

# #Chat GPT Version
# from pathlib import Path
# import re
# from typing import List

# def extract_error_codes(path: str) -> List[str]:
#     """Return sorted unique ERROR codes from log file."""
#     file_path = Path(path)
#     if not file_path.exists():
#         raise FileNotFoundError(file_path)

#     codes = set()
#     with file_path.open("r", encoding="utf-8") as f:
#         for line in f:
#             if "ERROR" not in line:
#                 continue
#             match = re.search(r"code=(\w+)", line)
#             if match:
#                 codes.add(match.group(1))

#     return sorted(codes)

# if __name__ == "__main__":
#     codes = extract_error_codes("/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/1_Basics_Foundation/sample_files/distinct_error_code.log")
#     if codes:
#         print(f"ERROR codes: {','.join(codes)}")
#     else:
#         print("No ERROR lines")
