Perfect 👍 — here’s a clean **Markdown Progress Sheet** with your Q1–Q5 answers, my feedback, and improved suggestions. You can drop this into your Git repo (e.g., `file_handling_practice.md`) to track your learning.

---

# 📘 Python File Handling Practice — Progress Sheet

---

## ✅ Q1 — Read & print file contents

**Your code**

```python
with open('notes.txt') as f:
   content = f.readlines()
   for line in content:
      print(line.strip())
```

**Feedback**

* ✔️ Correct use of `with open`.
* ✔️ Used `.strip()` for clean output.
* ⚠️ `readlines()` loads whole file into memory → not scalable.
* ⚠️ Could stream line-by-line (`for line in f`).

**Improved version**

```python
from pathlib import Path

def read_file(path: str) -> None:
    with Path(path).open("r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
```

---

## ✅ Q2 — Count lines (also show first & last)

**Your code**

```python
from pathlib import Path

def read_file(path: str) -> None:
    file_path = Path(path)

    if not file_path.exists():
        print(f"Error: {path} does not exist")
        return 
    
    with file_path.open('r', encoding='utf-8') as f:
        lines = f.readlines()
        print(len(lines))
```

**Feedback**

* ✔️ Counts lines correctly.
* ✔️ Good use of `Path`.
* ⚠️ `readlines()` not memory-friendly for large files.
* ⚠️ Missed printing first & last line.

**Improved version**

```python
from pathlib import Path
from collections import deque

def read_file(path: str) -> None:
    file_path = Path(path)
    if not file_path.is_file():
        print(f"Error: {path} does not exist")
        return

    first_line, count = None, 0
    last_line = deque(maxlen=1)

    with file_path.open("r", encoding="utf-8") as f:
        for line in f:
            if first_line is None:
                first_line = line.strip()
            last_line.append(line.strip())
            count += 1

    print(f"Total lines: {count}")
    if count > 0:
        print(f"First line: {first_line}")
        print(f"Last line: {last_line[0]}")
```

---

## ✅ Q3 — Write to a file

**Your code**

```python
with open('output.txt', 'w') as f:
    f.writelines(["Hello DevOps\n", "Welcome to Python\n", "File handling is fun"])

with open('output.txt') as output:
    content = output.read()
    print(content)
```

**Feedback**

* ✔️ Correct writing/reading.
* ⚠️ Last line missing `\n`.
* ⚠️ Safer to loop with `.write()`.
* ⚠️ Always specify `encoding="utf-8"`.

**Improved version**

```python
from pathlib import Path

def write_and_read(path: str) -> None:
    lines = ["Hello DevOps", "Welcome to Python", "File handling is fun"]

    file_path = Path(path)
    with file_path.open("w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    with file_path.open("r", encoding="utf-8") as f:
        print(f.read())
```

---

## ✅ Q4 — Append to a file

**Your code**

```python
from pathlib import Path

def append_with_read(path: str) -> None:
    file_path = Path(path)
    if not file_path.exists():
        print(f"File not found in the papth: {file_path}")

    with file_path.open("a", encoding="utf-8") as file_append:
        file_append.write("\nAppended line here")

    with file_path.open("r", encoding="utf-8") as file_read:
        print(file_read.read())
```

**Feedback**

* ✔️ Append works.
* ⚠️ Printing “file not found” is misleading → append mode creates it anyway.
* ⚠️ Always end new lines with `\n`.
* ⚠️ Typo (“papth”).

**Simplified version**

```python
from pathlib import Path

def append_line(path: str) -> None:
    file_path = Path(path)

    with file_path.open("a", encoding="utf-8") as f:
        f.write("Appended line here\n")

    with file_path.open("r", encoding="utf-8") as f:
        print(f.read())
```

---

## ✅ Q5 — Copy a file

**Your code**

```python
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
```

**Feedback**

* ✔️ Works fine for text files.
* ✔️ Streams line by line (good).
* ⚠️ For general copying (logs, binaries) → use **binary mode**.
* ⚠️ Better to use built-in `shutil.copyfile`.
* ⚠️ Read-back is good for practice but not needed in production.

**Improved version**

```python
from pathlib import Path
import shutil

def file_copy(source_path: str, dest_path: str) -> None:
    src = Path(source_path)
    dst = Path(dest_path)

    if not src.is_file():
        print(f"Error: {src} is not a file")
        return

    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)

    print(f"Copied {src} -> {dst}")
```

---

# 🏆 Summary

* Q1–Q5: ✅ Correct solutions, just need tweaks for scalability, robustness, and readability.
* Main interview focus: **large files, encoding, error handling, and portability**.
* You’re on track — strong start for Python file handling! 🚀

---

👉 Do you want me to now prepare the **next 5 exercises (Intermediate level: CSV & JSON)** in the same structured way so you can continue practicing?
