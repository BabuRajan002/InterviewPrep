# Append a content to a file
# with open('output.txt', 'a') as a:
#     a.write('\nAppended line here')

# with open('output.txt', 'r') as display_content:
#     content = display_content.read()
#     print(content)

from pathlib import Path

def append_with_read(path: str) -> None:
    file_path = Path(path)
    if not file_path.exists():
        print(f"File not found in the papth: {file_path}")

    with file_path.open("a", encoding="utf-8") as file_append:
        file_append.write("Appended line here\n")

    with file_path.open("r", encoding="utf-8") as file_read:
        print(file_read.read())

if __name__ == "__main__":
   append_with_read('output1.txt')