from pathlib import Path
import os, time

BASE = Path("./source_dir_q3")
FILES = [
    ("app.log", 3),       # 3 days old
    ("logs/debug.log", 45),   # 45 days old
    ("logs/error.log", 120),  # 120 days old
    ("notes.txt", 10),    # not a .log file
]

def touch_with_age(path: Path, days_old: int):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"sample content for {path.name}\n")
    # set last modified time to N days ago
    age_secs = days_old * 24 * 3600
    ts = time.time() - age_secs
    os.utime(path, (ts, ts))  # (atime, mtime)

if __name__ == "__main__":
    if BASE.exists():
        print(f"Cleaning up old {BASE} …")
        for p in sorted(BASE.rglob("*"), reverse=True):
            if p.is_file():
                p.unlink()
            elif p.is_dir():
                try:
                    p.rmdir()
                except OSError:
                    pass

    print(f"Creating {BASE} with test logs …")
    for fname, age in FILES:
        touch_with_age(BASE / fname, age)

    print("Done. Tree:")
    for p in sorted(BASE.rglob("*")):
        print(" -", p, "age_days ~", next((a for f, a in FILES if f == str(p.relative_to(BASE))), "?"))
