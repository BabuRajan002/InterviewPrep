from pathlib import Path
import os, time, shutil

BASE = Path("./source_dir_q6")
FILES = [
    ("recent.log", 5),         # 5 days old
    ("old.log", 40),           # 40 days old
    ("ancient.log", 100),      # 100 days old
    ("access.log", 40),        # 40 days old, should be excluded by *access.log
    ("misc.txt", 20),          # not a log
    ("logs/debug.log", 60),    # 60 days old
    ("logs/keep_error.log", 120), # should be excluded by keep_*
    ("logs/deep_recent.log", 2),
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
            print(f" - {p.relative_to(BASE)}  age_days ~ {days}")
