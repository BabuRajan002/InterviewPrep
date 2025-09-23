from pathlib import Path
from datetime import datetime, timezone

def delete_with_dryrun(path: str | Path, days: int, dry_run: bool=False) -> list[str]:
    dir_path = Path(path)

    if not dir_path.exists():
        raise FileNotFoundError(dir_path)
    
    now = datetime.now(timezone.utc)
    files = sorted((f for f in dir_path.rglob("*.log") if f.is_file() and not f.is_symlink()), key=lambda f: f.as_posix())
    
    deleted = []
    for f in files:
        mtime = datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc)
        if (now-mtime).days > days:
            if dry_run == True:
             deleted.append(str(f.relative_to(dir_path)))
            else:
             try:
                 f.unlink()
                 deleted.append(str(f.relative_to(dir_path)))
             except PermissionError:
                 print(f"unable to delete {f}: (permission denied)")
    return deleted
            
    

if __name__ == "__main__":
    deleted = delete_with_dryrun("./source_dir_q4", 30)
    print(deleted if deleted else "no files to be deleted")