import sys
import re 
from collections import Counter 
from pathlib import Path 

log_pattern = re.compile(
    r'service="(?P<service>[\w._-]+)"\s*status=(?P<code>\d{3})'
)

def parse_multi_log(path: str):
    filePath = Path(path)

    try:
        with open(filePath, 'r') as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue

                match = log_pattern.search(line)
                if match:
                    yield {
                        "service" : match.group("service"),
                        "code" : match.group("code")
                    }
    except FileNotFoundError:
        print(f"Unable to find the file {filePath}", file=sys.stderr)

if __name__ == "__main__":
    logPath = "/Users/babus/Desktop/repos/InterviewPrep/Python/SREInterviewPrep/Week1/Day5/multi.log"

    stats = {}

    for logentry in parse_multi_log(logPath):
        service = logentry['service']
        code = logentry['code']

        if service not in stats:
            stats[service] = {"total": 0, "errors": 0}
        
        stats[service]["total"] += 1
        if code.startswith('5'):
            stats[service]["errors"] += 1
    
    print("--- SERVICE SLO REPORT ---")

    for service, data in stats.items():
        total = data["total"]
        errors = data["errors"]

        error_rate = (errors / total * 100) if total > 0 else 0.0
        print(f"{service:<15} : {error_rate:.1f}% Error Rate")
    
    print("--------------------------")



