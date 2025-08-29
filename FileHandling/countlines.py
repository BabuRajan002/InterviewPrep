#Count the number of lines in a file
# with open('notes.txt') as f:
#     lines = f.readlines()
#     print(len(lines))

from pathlib import Path
from collections import deque

def read_file(path: str) -> None:
    file_path = Path(path)

    if not file_path.exists():
        print(f"Error: {path} does not exist")
        return 
    
    with file_path.open('r', encoding='utf-8') as f:
        first_line = None
        last_line = deque(maxlen=1)
        count = 0

        for line in f:
            if first_line is None:
                first_line = line.strip()
            last_line.append(line.strip())
            count += 1
        
    print(f"Total lines: {count}")
    if count > 0:
        print(f"first line is: {first_line}")
        print(f"last line is: {last_line[0]}")
        

if __name__ == "__main__":
    read_file("notes.txt")


