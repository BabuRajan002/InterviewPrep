from pathlib import Path
from datetime import datetime, timezone
import fnmatch

def max_delete(path: str, days, max_delete_days, excludes, dry_run=True):
    dir_path = Path(path)

    if not dir_path.exists():
        raise FileNotFoundError(dir_path)
    
    now = datetime.now(timezone.utc)
    files = sorted((f for f in dir_path.rglob("*.log") if f.is_file() and not f.is_symlink()), key=lambda f: f.as_posix())
    candidates = []
    for f in files:
       rel = str(f.relative_to(dir_path))
       mtime = datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc)
       old_enough = (now-mtime).days > days
       excluded = any(fnmatch.fnmatch(f.name, pat) for pat in excludes)

       if not old_enough or excluded:
           continue
       
       if dry_run:
            candidates.append(rel)
       else: 
           try:
             candidates.append(rel)
             f.unlink()
           except PermissionError:
             print(f"SKIP {f} (Permission denied)")
    if max_delete_days is not None:
      return candidates[:max_delete_days]
    else:
       return f"Max delete days are none"

if __name__ == "__main__":
   print(max_delete("./source_dir_q6", 30, 2, ["access.log", "keep*.log"], True))
