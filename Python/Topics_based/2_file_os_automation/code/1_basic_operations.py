import os
from pathlib import Path
import shutil


print(os.listdir("."))

for root, dirs, files in os.walk("."):
    for f in files:
        print(os.path.join(root, f))

print(os.path.exists("1_list_ir.py"))

os.makedirs("demo_dir", exist_ok=True)
os.rmdir("demo_dir")

print(os.environ.get("Home"))

p = Path("test.txt")
p.touch()

os.chmod("test.txt", 0o755)

with open("test.txt", "w", encoding="utf-8") as f:
     lines = [
         "Hello, DevOps!",
         "I am learning Python",
         "I am very good at Python"
     ]    

     for line in lines:
         f.write(line + "\n")

#Copy file
shutil.copy("test.txt", "backup.txt")
#Move or rename a file
shutil.move("backup.txt", "backup_file.txt")