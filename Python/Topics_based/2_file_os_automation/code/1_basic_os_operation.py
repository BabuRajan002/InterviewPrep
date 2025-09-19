import os
from pathlib import Path

# List files in a directory
print(os.listdir("."))

# Walk recursively (like `find .`)
for root, dirs, files in os.walk("."):
    for f in files:
        print(os.path.join(root, f))

# Check if path exists
print(os.path.exists("myfile.txt"))

# Make/remove directories
os.makedirs("demo_dir", exist_ok=True)
os.rmdir("demo_dir")

# Get environment variables
print(os.environ.get("HOME"))

# Permissions
p = Path("test.txt")
p.touch()  # create empty file
os.chmod("test.txt", 0o644)  # rw-r--r--
