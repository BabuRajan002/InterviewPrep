from pathlib import Path
import fnmatch
from datetime import datetime, timezone

def delete_with_excludes(path: str, days, exclude_files, dry_run=False,):
    patterns = exclude_files
    dir_path = Path(path)
    
    if not dir_path.exists():
        raise FileNotFoundError(dir_path)
    
    #Helper fucntion
    def should_exclude(name: str, patterns) -> bool:
        return any(fnmatch.fnmatch(name, pat) for pat in patterns)
    
    now = datetime.now(timezone.utc)
    files = sorted((f for f in dir_path.rglob("*.log") if f.is_file() and not f.is_symlink()), key=lambda f: f.as_posix())
    tobe_deleted = []
    for f in files:
        mtime = datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc)
        rel = str(f.relative_to(dir_path))
        if (now-mtime).days > days:
           if dry_run:
               if should_exclude(rel, patterns)==False:               
                 tobe_deleted.append(rel)
           else:               
               try:
                   if should_exclude(rel, patterns) == False:
                    f.unlink()
                    tobe_deleted.append(rel)
               except PermissionError:
                   print(f"Unable to delete")   


    
    return tobe_deleted

if __name__ == "__main__":
    print(delete_with_excludes("./source_dir_q6", 30, ["*access.log", "logs/keep_*"], True))


# #Chat GPT Verison:

# from pathlib import Path
# from datetime import datetime, timezone
# from typing import List, Optional
# import fnmatch

# def delete_with_excludes(
#     path: str | Path,
#     days: int,
#     excludes: Optional[list[str]] = None,
#     dry_run: bool = False,
# ) -> List[str]:
#     """
#     Delete (or preview) .log files older than `days` under `path`.
#     Exclusions are matched against the file's relative path (e.g. 'logs/debug.log').
#     Returns a sorted list of relative paths that were (or would be) deleted.
#     """
#     dir_path = Path(path)
#     if not dir_path.exists():
#         raise FileNotFoundError(dir_path)

#     patterns = excludes or []
#     now = datetime.now(timezone.utc)

#     files = sorted(
#         (p for p in dir_path.rglob("*.log") if p.is_file() and not p.is_symlink()),
#         key=lambda p: p.as_posix(),
#     )

#     removed: List[str] = []
#     for f in files:
#         rel = str(f.relative_to(dir_path))
#         mtime = datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc)
#         old_enough = (now - mtime).days > days
#         excluded = any(fnmatch.fnmatch(rel, pat) for pat in patterns)
#         if not old_enough or excluded:
#             continue

#         if dry_run:
#             removed.append(rel)
#         else:
#             try:
#                 f.unlink()
#                 removed.append(rel)
#             except PermissionError:
#                 # optional: collect/report skipped perms elsewhere
#                 pass

#     return removed

# if __name__ == "__main__":
#     print(delete_with_excludes("./source_dir_q6", 30, ["*access.log", "logs/keep_*"], True))
