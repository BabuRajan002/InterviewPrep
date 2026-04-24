import sys
import json
from collections import Counter 
from pathlib import Path 

def latency_measure(path: str):
    filePath = Path(path)
    try: 

        with open(filePath, 'r') as file:
            data = json.load(file)

            for item in data:
                latency = item.get('latency_ms', 0)
                status = item.get('status', 'unknown')
                if status != 'healthy' and latency > 200:           
                    yield {
                        "service": item['service'],
                        "status" : item['status'],
                        "latency_ms" : item['latency_ms'],
                        "region" : item['region']
                    }
    
    except FileNotFoundError:
        print(f"File is not found {filePath}", file=sys.stderr)               


if __name__ == "__main__":
    logPath = "/Users/babus/Desktop/repos/InterviewPrep/Python/SREInterviewPrep/Nasdaq/json.log"
    items = latency_measure(logPath)
    count = 0

    print(f"--- CRITICAL SERVICE ALERTS ---")

    for alert in items:
        count += 1
        print(f"Service: {alert['service']}")
        print(f"Status: {alert['status']}")
        print(f"Latency: {alert['latency_ms']}")
        print(f"Region: {alert['region']}")
        print()
    print("--------------------------------------")

    print(f"Total Issues found: {count}")
