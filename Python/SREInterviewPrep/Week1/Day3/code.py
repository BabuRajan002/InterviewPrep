import re
import sys 
from collections import Counter
from pathlib import Path

LOG_PATTERN = re.compile (
    r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(?:GET|POST|PUT|DELETE)\s(?P<uri>\S+).*?(?:HTTP/1.1")\s(?P<return_code>\d{3})'
)


def get_max_hits(path: str):
    filepath = Path(path)

    try:
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                match = LOG_PATTERN.search(line)
                if match:
                    yield match.groupdict()               
  
    except FileNotFoundError:
        print(f"Error: {filepath} not found", file=sys.stderr)

if __name__ == "__main__":
    logFile = '/Users/babus/Desktop/repos/InterviewPrep/Python/SREInterviewPrep/Week1/Day3/access.log'

    ipCounts = Counter()
    uriCounts = Counter()
    statusCodeCounts = Counter()

    for entry in get_max_hits(logFile):
        ipCounts.update([entry['ip']])
        uriCounts.update([entry['uri']])
        statusCodeCounts.update([entry['return_code']])
    
    print("\n[Top 5 IP addresses]")
    for ip, count in ipCounts.most_common(5):
        print(f"{ip:<18} - {count} requests")
    
    print("\n[Top 5 Requested Paths]")
    for uri, count in uriCounts.most_common(5):
        print(f"{uri:<18} - {count} hits")
    
    print("\n[HTTP Status Codes]")
    for code, count in statusCodeCounts.most_common(5):
        print(f"- {code}: {count}")

