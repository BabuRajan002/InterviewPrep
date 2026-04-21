import re 
import sys 
import json
from pathlib import Path

LOG_PATTERN = re.compile (
    r'\[(?P<timestamp>.*?)\]\s+(?P<level>ERROR|INFO|WARN)\s+(?P<message>.*)'
)

def get_error_logs(path: str):
    filePath = Path(path)
    try:
        with open(filePath, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                match = LOG_PATTERN.search(line)

                if not match:
                    continue

                if match.group('level') == 'ERROR':
                    yield {
                        "timestamp" : match.group('timestamp'),
                        "message" : match.group('message')
                    }
    except FileNotFoundError:
        print(f"ERROR: {filePath} not found", file=sys.stderr)

if __name__ == "__main__":
    log_file = "/Users/babus/Desktop/repos/InterviewPrep/Python/SREInterviewPrep/Week1/Day2/app.log"

    # error_list = list(get_error_logs(log_file))

    # print(json.dumps(error_list, indent=4))
    for errordata in get_error_logs(log_file):
        timestamp = errordata['timestamp']
        message = errordata['message']

        print(f"[{timestamp}] ALERT: {message}")
        
