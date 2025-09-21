from pathlib import Path
import glob
from typing import List

def recursive_log_files(path: str | Path="./source_dir") -> List[Path]:
    dir_path = Path(path)

    if not dir_path.exists():
        raise FileNotFoundError(dir_path)
    
    logs = [f for f in dir_path.rglob("*.log") if f.is_file()] #Recursive output
    
    return sorted(logs, key=lambda d: d.as_posix() ) #Sorts the result with its relative path! Not only with the filename
    

if __name__ == "__main__":
    log_files = recursive_log_files("./source_dir")
    print([str(p.relative_to("./source_dir")) for p in log_files] if log_files else "No log files found")


