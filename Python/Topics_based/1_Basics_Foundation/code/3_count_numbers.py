from pathlib import Path

def count_number(path: str) -> tuple[int, int]:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(file_path)
    try:    
      with file_path.open('r', encoding="utf-8") as num_file:

        num_list = []
        empty_tuple = ()
        for line in num_file:
            line = line.strip()
            if not line or line.startswith('#'):
                 continue
            try:
               num_list.append(int(line))
            except ValueError:
               print(f"Found an invalid number and continuing to next number")
               continue
        if not num_list:
           print(f"File is empty")
        result = sum(num_list)
        new_tuple = empty_tuple + (result, len(num_list))
        return new_tuple 
    except Exception as e:
      print(f"found an error{e}")
      return(0,0)

if __name__ == "__main__":
    print(count_number("/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/1_Basics_Foundation/sample_files/numbers.txt"))

# # Chat GPT Version:
# from pathlib import Path
# from typing import Tuple

# def sum_numbers(path: str) -> Tuple[int, int]:
#     """Return (sum, count) of integers in file, skipping blanks and comments."""
#     file_path = Path(path)
#     if not file_path.exists():
#         raise FileNotFoundError(file_path)

#     numbers = []
#     with file_path.open("r", encoding="utf-8") as f:
#         for line in f:
#             line = line.strip()
#             if not line or line.startswith("#"):
#                 continue
#             try:
#                 numbers.append(int(line))
#             except ValueError:
#                 # Skip malformed numbers
#                 continue

#     return (sum(numbers), len(numbers))

# if __name__ == "__main__":
#     total, count = sum_numbers("numbers.txt")
#     print(f"Sum = {total}, Count = {count}")
