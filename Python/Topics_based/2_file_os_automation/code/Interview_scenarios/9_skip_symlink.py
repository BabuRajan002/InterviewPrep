from pathlib import Path
from datetime import datetime, timezone
import fnmatch
from typing import List


def skip_symlink(path: str, days, max_delete_days, exclude, dry_run=True): 
    dir_path = Path("./source_dir_q9")

    if not dir_path.exists():
        raise FileNotFoundError(dir_path)
    
    now = datetime.now(timezone.utc)

    files = sorted((f for f in dir_path.rglob("*.log")), key=lambda f: f.as_posix())
    skipped: List[tuple[str, str]] = []
    old_days = []
    candidates = []
    for f in files:
      if f.is_symlink():
         skipped.append((str(f.relative_to(dir_path)), "symlink"))
         continue
      if f.is_file():   
         mtime = datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc)
         old_enough = (now - mtime).days > days
         excluded = any(fnmatch.fnmatch(f.name, pat) for pat in exclude)
         if not old_enough or excluded:
             continue
         candidates.append(f)
         old_days.append((now-mtime).days)

    
    if max_delete_days is not None:
       candidates = candidates[:max_delete_days]
       old_days = old_days[:max_delete_days]
    
    rels: List[str] = [str(p.relative_to(dir_path)) for p in candidates]
    removed = []

    if dry_run:
       return (rels, dry_run, old_days), skipped
    else:
       try:
        for f in candidates:
          f.unlink()
          removed.append(str(f.relative_to(dir_path)))
       except PermissionError:
          pass
    
    return(removed, dry_run, old_days), skipped
     

if __name__ == "__main__":
    log_bundle, skipped_files = skip_symlink("./source_dir_q9", 30, 4, ["access.log", "keep*.log"], True)
    log_files, val, days = log_bundle
    acted = []
    for file, day in zip(log_files, days):
        if val:
            acted.append((file, day, "DRYRUN"))
    print(acted)
    print(skipped_files)
