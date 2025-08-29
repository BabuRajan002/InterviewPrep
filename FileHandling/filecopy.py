# Copy a content from one file to another file 

# source_file = "notes.txt"
# destination_file = "notes_copy.txt"

# with open(source_file, "r") as f_source, open(destination_file, "w") as f_destination:
#     lines = f_source.readlines()
#     for line in lines:
#         f_destination.write(line.strip()+'\n')

# with open(destination_file) as f:
#     content = f.read()
#     print(content)

from pathlib import Path

def file_copy(source_path: str, dest_path: str) -> None:
    source_file_path = Path(source_path)
    dest_file_path = Path(dest_path)

    if not source_file_path.is_file():
       print(f"Provide the proper source file")
       return
    
    with source_file_path.open("r", encoding="utf-8") as f_source, dest_file_path.open("w", encoding="utf-8") as f_dest:
        for line in f_source:
            f_dest.write(line)

    with dest_file_path.open("r", encoding="utf-8") as f_dest:
        print(f_dest.read())
    
    print(f"copied {source_file_path} -> {dest_file_path}")

if __name__ == "__main__":
    file_copy("notes.txt", "new_output.txt")    

    
