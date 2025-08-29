# Open and read the lines in a file
with open('notes.txt') as f:
   content = f.readlines()
   for line in content:
      print(line.strip())

#readlines() loads entire file into memory. Fine for tiny files like notes.txt, but if I ask “what if it’s a 10GB log file?” this won’t scale. A better way is to stream line by line.
    # for line in f:
    #     print(line.strip())

## Suggestion from Interview Point of View 

# from pathlib import Path

# def read_file(path: str) -> None:
#     file_path = Path(path)
#     if not file_path.exists():
#         print(f"Error: {path} does not exist")
#         return

#     with file_path.open("r", encoding="utf-8") as f:
#         for line in f:
#             print(line.strip())

# if __name__ == "__main__":
#     read_file("notes.txt")
