from pathlib import Path
import os, time, shutil, stat

BASE = Path("./source_dir_q9")

FILES = [
    ("old.log", 40),            # regular old file
    ("logs/protected.log", 60), # will chmod 000
]

def touch_with_age(path: Path, days_old: int):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"Sample {path.name}\n")
    ts = time.time() - (days_old * 24 * 3600)
    os.utime(path, (ts, ts))  # set atime/mtime

if __name__ == "__main__":
    if BASE.exists():
        print(f"Cleaning up old {BASE} …")
        shutil.rmtree(BASE)

    print(f"Creating {BASE} …")
    for fname, age in FILES:
        touch_with_age(BASE / fname, age)

    # Add a symlink pointing to old.log
    symlink_path = BASE / "symlink.log"
    target = BASE / "old.log"
    symlink_path.symlink_to(target)
    print(f"Created symlink {symlink_path} -> {target}")

    # Protect logs/protected.log so unlink raises PermissionError
    prot = BASE / "logs/protected.log"
    prot.chmod(0)  # no permissions

    print("Done. Tree:")
    for p in sorted(BASE.rglob("*")):
        if p.is_file() or p.is_symlink():
            print(f" - {p.relative_to(BASE)} -> {'symlink' if p.is_symlink() else 'file'}")
