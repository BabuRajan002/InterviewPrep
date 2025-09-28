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
    old_days = []
    for f in files:       
       mtime = datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc)
       old_enough = (now-mtime).days > days       
       excluded = any(fnmatch.fnmatch(f.name, pat) for pat in excludes)

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
        return (rels, dry_run, old_days)
    else:
        for f in candidates:
            try:
                f.unlink()
                removed.append(str(f.relative_to(dir_path)))
            except PermissionError:
                pass
    
    return (removed, dry_run, old_days)


if __name__ == "__main__":
    log_files, val, days = max_delete("./source_dir_q6", 30, 4, ["access.log", "keep*.log"], True)
    now_date = datetime.now(timezone.utc).isoformat(timespec="seconds").replace('+00:00', 'Z')
    for file, day in zip(log_files, days):
     with open('./cleanuplog.txt', 'a', encoding='utf-8') as f:
        f.write(f"{now_date} {'DRYRUN' if val else 'DELETE'} {file} age={day}\n")

# #Chat GPT Version
# from pathlib import Path
# from datetime import datetime, timezone
# from typing import List, Optional, Tuple
# import fnmatch

# ISO = "%Y-%m-%dT%H:%M:%SZ"

# def delete_with_max_and_logging(
#     path: str | Path,
#     days: int,
#     excludes: Optional[list[str]] = None,
#     max_delete: Optional[int] = None,
#     dry_run: bool = False,
#     log_path: Optional[str | Path] = "cleanup.log",
# ) -> List[Tuple[str, int]]:
#     """
#     Delete (or preview) .log files older than `days`, skipping excludes.
#     Returns a list of (relative_path, age_days) for files acted on (or would act on).
#     Logs each action if log_path is provided.
#     """
#     dir_path = Path(path)
#     if not dir_path.exists():
#         raise FileNotFoundError(dir_path)

#     patterns = excludes or []
#     now = datetime.now(timezone.utc)

#     # Build candidate (path, age_days) pairs deterministically
#     files = sorted(
#         (p for p in dir_path.rglob("*.log") if p.is_file() and not p.is_symlink()),
#         key=lambda p: p.as_posix(),
#     )
#     pairs: List[Tuple[Path, int]] = []
#     for f in files:
#         age_days = (now - datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc)).days
#         if age_days <= days:
#             continue
#         if any(fnmatch.fnmatch(f.name, pat) for pat in patterns):
#             continue
#         pairs.append((f, age_days))

#     # Apply max limit BEFORE acting
#     if max_delete is not None:
#         pairs = pairs[:max_delete]

#     # Prepare logger
#     def stamp() -> str:
#         return datetime.now(timezone.utc).strftime(ISO)

#     acted: List[Tuple[str, int]] = []

#     # Open log file once if needed
#     log_file = Path(log_path) if log_path is not None else None
#     log_fh = log_file.open("a", encoding="utf-8") if log_file else None
#     try:
#         for f, age in pairs:
#             rel = str(f.relative_to(dir_path))
#             action = "DRYRUN" if dry_run else "DELETE"

#             if not dry_run:
#                 try:
#                     f.unlink()
#                 except PermissionError:
#                     # Optional: log a SKIP line
#                     if log_fh:
#                         log_fh.write(f"{stamp()} SKIP   {rel} reason=permission\n")
#                     continue

#             acted.append((rel, age))
#             if log_fh:
#                 log_fh.write(f"{stamp()} {action} {rel} age={age}\n")
#     finally:
#         if log_fh:
#             log_fh.close()

#     return acted

# if __name__ == "__main__":
#     # Dry-run example
#     print(
#         delete_with_max_and_logging(
#             "./source_dir_q6",
#             days=30,
#             excludes=["*access.log", "keep*.log"],
#             max_delete=4,
#             dry_run=True,
#             log_path="cleanup.log",
#         )
#     )




