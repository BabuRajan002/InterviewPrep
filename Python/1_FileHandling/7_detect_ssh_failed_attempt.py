#My Version
from pathlib import Path
import re
from collections import Counter

def detect_ssh_failed_attempt(path: str) -> None:
    file_path = Path(path)

    if not file_path.exists():
        print(f"Provide the proper file path: {file_path}")
        return 
    
    with file_path.open('r', encoding="utf-8") as file:
        big_lists = []
        final_address = []     
        ip_addr = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        for line in file:
            if "Failed" in line:
                big_lists.append(re.findall(ip_addr, line)) 

        for lst in big_lists:
            for element in lst:
                final_address.append(element)

        ip_counts = Counter(final_address)         
        print(ip_counts)

        for key, value in ip_counts.items():
            count = int(value)
            if count >= 3:
                print(f"{key} {value}")

     
                  

if __name__ == "__main__":
    detect_ssh_failed_attempt("/Users/babus/Desktop/repos/InterviewPrep/Python/1_FileHandling/sample_files/detect_ssh_failed_attempts.log")


#ChatGPT Version
from pathlib import Path
import re
from collections import Counter

# Example line:
# Aug 18 10:12:05 host sshd[1024]: Failed password for invalid user admin from 198.51.100.23 port 55210 ssh2
FAILED_RE = re.compile(
    r"Failed password for (?:invalid user \S+|\S+) from "
    r"(?P<ip>(?:\d{1,3}\.){3}\d{1,3})\b"
)

def detect_ssh_failed_attempt(path: str, threshold: int = 3) -> None:
    p = Path(path)
    if not p.is_file():
        print(f"Error: {p} not found")
        return

    counts = Counter()

    with p.open("r", encoding="utf-8") as fh:
        for line in fh:
            m = FAILED_RE.search(line)
            if not m:
                continue
            counts[m.group("ip")] += 1

    # Print full counts (optional)
    # print(counts)

    # Suspicious: >= threshold, sorted by attempts desc then IP
    suspicious = sorted(
        ((ip, c) for ip, c in counts.items() if c >= threshold),
        key=lambda x: (-x[1], x[0])
    )

    for ip, c in suspicious:
        print(f"{ip} {c}")

if __name__ == "__main__":
    detect_ssh_failed_attempt("syslog.log", threshold=3)
