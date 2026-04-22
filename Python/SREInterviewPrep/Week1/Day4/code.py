import re 
import sys
from collections import Counter 
from pathlib import Path 

LOG_PATTERN = re.compile (
    r'.*\s(?P<resp_time>\d+\.\d+)$'
)

def get_resp_time(path: str):
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
                else:
                  yield {
                        "resp_time" : match.group('resp_time')
                   } 
    except FileNotFoundError:
       print(f"Error {filePath} not found", file=sys.stderr)

if __name__ == "__main__":
   logPath = "/Users/babus/Desktop/repos/InterviewPrep/Python/SREInterviewPrep/Week1/Day4/nginx.log"

   totalSum = 0.0
   totalCount = 0
   maxLatency = 0.0
   totalExceed = 0
   for rtime in get_resp_time(logPath):
      latency = float(rtime['resp_time'])
      totalSum += latency
      totalCount += 1
      if latency > maxLatency:
         maxLatency = latency
      
      if latency > 0.5:
         totalExceed += 1         
    
   avgLatency = totalSum / totalCount if totalCount > 0 else 0 
   percent_breached = (totalExceed / totalCount) * 100 if totalCount > 0 else 0 
   print("\n --- SRE Latency Performance Report ---")
   
   print(f"\nTotal Requests Processed: {totalCount}")
   print(f"Average Latency: {avgLatency:.3f}s")
   print(f"Maximum Latency: {maxLatency:.3f}s")


   print("\n [Threshold Analysis]")
   print(f"\nRequests exceeding 0.5s: {totalExceed}")
   print(f"Percentage Breach: {percent_breached:.1f}%")
   print(f"\n --- Status: SLO VIOLATED ---")