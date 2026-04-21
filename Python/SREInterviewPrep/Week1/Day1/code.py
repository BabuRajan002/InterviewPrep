import sys
from collections import Counter

def get_log_data(filepath):
    try:
        with open(filepath, 'r') as f:
            for line in f:
                # 1. Skip truly empty lines immediately
                line = line.strip()
                if not line:
                    continue
                
                # 2. Split into parts to avoid the "informed" vs "INFO" bug
                parts = line.split()
                
                # 3. Handle malformed lines (Expect: Date, Time, Level, Message)
                if len(parts) < 3:
                    print(f"Malformed line: {line[:20]}...", file=sys.stderr)
                    continue              
                else:
                    level = parts[2].upper()
                    message = " ".join(parts[3:])
                
                yield level, message

    except FileNotFoundError:
        print(f"Critical: File {filepath} not found.", file=sys.stderr)

if __name__ == "__main__":
    log_path = "app.log"
    counts = Counter()
    errors = []

    for level, msg in get_log_data(log_path):
        counts[level] += 1
        # Bonus: Anthropic/Apple often ask to "collect" specific data
        if level == "ERROR":
            errors.append(msg)

    print(f"Summary: {dict(counts)}")
    print(f"Sample Errors: {errors[:2]}")