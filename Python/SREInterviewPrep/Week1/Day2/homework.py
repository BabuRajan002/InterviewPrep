import re
import sys 
import json
from pathlib import Path

LOG_PATTERN = re.compile (
    r'\[(?P<time>\d{4}[/-]\d{2}[/-]\d{2} \d{2}:\d{2}:\d{2})\] (?P<level>\w+) - (?P<msg>.*?)(?: \(ReqID: (?P<req_id>\d+)\))?$'
      
)

def get_error_log(path: str):
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

                if match.group('level').upper() == 'ERROR':
                    yield {
                        "time" : match.group('time'),
                        "level" : match.group('level'),
                        "req_id" : match.group('req_id'),
                        "msg" : match.group('msg')
                    }
    except FileNotFoundError:
        print(f"Error: {filePath} not found", file=sys.stderr)

if __name__ == "__main__":
    logfile = "/Users/babus/Desktop/repos/InterviewPrep/Python/SREInterviewPrep/Week1/Day2/audit.log"

    for errordata in get_error_log(logfile):
        time = errordata['time']
        level = errordata['level']
        req_id = errordata['req_id']
        msg = errordata['msg']
    
        print(f'"time" : {time}, "level": {level.upper()}, "req_id" : {req_id}, "msg" : {msg}')




