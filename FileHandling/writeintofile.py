# Write a content to a file
# with open('output.txt', 'w') as f:
#     f.writelines(["Hello DevOps\n", "Welcome to Python\n", "File handling is fun"])

# with open('output.txt') as output:
#     content = output.read()
#     print(content) 

from pathlib import Path

def write_file(path: str) -> None:
    file_path = Path(path)

    lines = [
        "Hello Devops",
        "Welcome to Python",
        "File handling us fun",
    ]

    with file_path.open("w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + '\n')
    
    with file_path.open("r", encoding="utf-8") as file_read:
           print(file_read.read())
    

if __name__ == "__main__":
     write_file("output1.txt")
  