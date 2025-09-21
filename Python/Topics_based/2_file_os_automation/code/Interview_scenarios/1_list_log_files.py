from pathlib import Path
import os
import glob

def list_log_files(path: str="./source_dir"):
    dir_path = Path(path)

    if not dir_path.exists():
        raise FileNotFoundError(dir_path)
    
    logs = [f for f in dir_path.glob("*.log") if f.is_file()] #Non-recursive
    return sorted(logs, key=lambda d: d.name)


if __name__ == "__main__":
    log_files = list_log_files("./source_dir")
    # if log_files:
    #     print(log_files)
    # else:
    #     print("No log files found")
    print( [str(f.relative_to("./source_dir")) for f in log_files] if log_files else "No log files found") #Comprehensive loop
    

# #ChatGPT Version
# from pathlib import Path
# from typing import List

# def list_log_files(path: str | Path = "./source_dir") -> List[Path]:
#     """Return non-recursive list of .log files in the given directory, sorted."""
#     dir_path = Path(path)
#     if not dir_path.exists():
#         raise FileNotFoundError(dir_path)
#     logs = [p for p in dir_path.glob("*.log") if p.is_file()]
#     return sorted(logs, key=lambda p: p.name)

# if __name__ == "__main__":
#     files = list_log_files("./source_dir")
#     print([str(p) for p in files] if files else "No log files found")
