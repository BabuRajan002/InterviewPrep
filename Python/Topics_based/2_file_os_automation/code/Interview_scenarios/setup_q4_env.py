from pathlib import Path
import os, time, shutil

BASE = Path("./source_dir_q4")
FILES = [
    ("recent.log", 5),      # 5 days old
    ("old.log", 40),        # 40 days old
    ("ancient.log", 100),   # 100 days old
    ("misc.txt", 50),       # not a log file
    ("logs/deep_old.log", 60),   # nested .log
    ("logs/deep_recent.log", 2), # nested .log
]

def touch_with_age(path: Path, days_old: int):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"Sample {path.name}\n")
    age_secs = days_old * 24 * 3600
    ts = time.time() - age_secs
    os.utime(path, (ts, ts))  # (atime, mtime)

if __name__ == "__main__":
    if BASE.exists():
        print(f"Cleaning up old {BASE} …")
        shutil.rmtree(BASE)

    print(f"Creating {BASE} with test logs …")
    for fname, age in FILES:
        touch_with_age(BASE / fname, age)

    print("Done. Tree:")
    for p in sorted(BASE.rglob("*")):
        if p.is_file():
            days = next((a for f, a in FILES if f == str(p.relative_to(BASE))), "?")
            print(f" - {p}  age_days ~ {days}")
