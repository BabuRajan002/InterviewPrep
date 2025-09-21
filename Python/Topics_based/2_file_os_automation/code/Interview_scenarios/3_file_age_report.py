from pathlib import Path
import glob
from typing import List
from datetime import datetime, timezone

def file_age_report(path: str | Path="./source_dir_q3") -> List[tuple[str, str, int]]:
    dir_path = Path(path)

    if not dir_path.exists():
        raise FileNotFoundError(dir_path)
    
    now = datetime.now(timezone.utc)
    files = sorted((f for f in dir_path.rglob("*.log") if f.is_file()), key=lambda f: f.as_posix())
    
    list_of_files: List[tuple[str, str, int]] = []
    for f in files:      
      modified_date = datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc)      
      file_age = (now - modified_date).days
    #   print(str(f.relative_to("./source_dir_q3")), file_age.days)
      list_of_files.append((str(f.relative_to(dir_path)), modified_date.isoformat().replace('+00:00', 'Z'), file_age.days))
    return list_of_files


if __name__ == "__main__":
    files_details = file_age_report("./source_dir_q3")
    if files_details:
     for file in files_details:
        print(file)
    else:
       print("empty dir")
    

    
    