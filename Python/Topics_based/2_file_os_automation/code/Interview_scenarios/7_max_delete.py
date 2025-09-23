from pathlib import Path
from datetime import datetime, timezone
import fnmatch
from typing import List

def max_delete(path: str, days, max_delete_days, excludes, dry_run=True):
    dir_path = Path(path)

    if not dir_path.exists():
        raise FileNotFoundError(dir_path)
    
    now = datetime.now(timezone.utc)
    files = sorted((f for f in dir_path.rglob("*.log") if f.is_file() and not f.is_symlink()), key=lambda f: f.as_posix())
    candidates = []
    for f in files:       
       mtime = datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc)
       old_enough = (now-mtime).days > days
       excluded = any(fnmatch.fnmatch(f.name, pat) for pat in excludes)

       if not old_enough or excluded:
           continue
       candidates.append(f)
    if max_delete_days is not None:
       candidates = candidates[:max_delete_days]
    
    rels: List[str] = [str(p.relative_to(dir_path)) for p in candidates]
    removed = []
    if dry_run:
        return rels
    else:
        for f in candidates:
            try:
                f.unlink()
                removed.append(str(f.relative_to(dir_path)))
            except PermissionError:
                pass
    
    return removed      


if __name__ == "__main__":
   print(max_delete("./source_dir_q6", 30, 4, ["access.log", "keep*.log"], True))
