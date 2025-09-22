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
    
    out: List[tuple[str, str, int]] = []
    for f in files:
        mtime = datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc)
        age_days = (now - mtime).days
        rel = str(f.relative_to(dir_path))
        iso = mtime.isoformat().replace("+00:00", "Z")  # ISO format
        out.append((rel, iso, age_days))
    return out


if __name__ == "__main__":
   for rel, iso, days in file_age_report("./source_dir_q3"):
       print(f"{rel:20} {iso} {days} days")

    

    
    