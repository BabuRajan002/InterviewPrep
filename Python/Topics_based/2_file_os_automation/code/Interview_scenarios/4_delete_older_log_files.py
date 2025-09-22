from pathlib import Path
from typing import List
from datetime import datetime, timezone


def delete_older_log_files(path: str, age) -> List[Path]:
    dir_path = Path(path)

    if not dir_path.exists():
        raise FileNotFoundError(dir_path)
    
    now = datetime.now(timezone.utc)

    files = sorted((f for f in dir_path.rglob("*.log") if f.is_file() and not f.is_symlink()), key=lambda f: f.as_posix())
    
    deleted_files = []
    for f in files:
       mtime = datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc)
       if (now - mtime).days > age:           
           try:
             f.unlink()
             deleted_files.append(str(f.relative_to(dir_path)))
           except:
               raise PermissionError(f)
    return deleted_files
       
if __name__ == "__main__":
    older_files = delete_older_log_files("./source_dir_q4", 30)
    print(older_files if older_files else "No old files deleted")


    
    
