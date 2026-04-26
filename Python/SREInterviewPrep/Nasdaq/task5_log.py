import sys
import re
from pathlib import Path

# Patterns are correct, but simplified for the report requirements
Latency_Pattern = re.compile(r'client:\s*(?P<ip>[\d.]+).*?duration:\s*(?P<duration>\d+)')
Budget_Audit = re.compile(r'Project\s*"(?P<project>[\w-]+)"\s*cost:\s*(?P<cost>[\d.]+)')
Pod_Status = re.compile(r'Pod\s*"(?P<podname>[\w.-]+)"\s*(?P<status>OOMKilled)')

def log_dump(path: str):
    filePath = Path(path)
    try:
        with open(filePath, 'r') as f:
            for line in f:
                # Check for matches independently
                m1 = Latency_Pattern.search(line)
                m2 = Budget_Audit.search(line)
                m3 = Pod_Status.search(line)

                if m1: yield {"type": "latency", "ip": m1.group("ip"), "val": int(m1.group("duration"))}
                if m2: yield {"type": "budget", "project": m2.group("project"), "val": float(m2.group("cost"))}
                if m3: yield {"type": "error", "pod": m3.group("podname")}
    except FileNotFoundError:
        print(f"Error: {filePath} not found", file=sys.stderr)

if __name__ == "__main__":
    logPath = "dump.log" # Update with your full path
    
    # Accumulators for the report
    latencies = []
    total_cost = 0.0
    oom_pods = []

    for data in log_dump(logPath):
        if data["type"] == "latency":
            latencies.append(data["val"])
        elif data["type"] == "budget":
            total_cost += data["val"]
        elif data["type"] == "error":
            oom_pods.append(data["pod"])

    # --- GENERATE REPORT ---
    print("--- PRODUCTION STATUS REPORT ---")
    
    # 1. Latency Report
    if latencies:
        avg_latency = sum(latencies) / len(latencies)
        print(f"Average Latency: {avg_latency:.2f}ms")
    
    # 2. Budget Report
    print(f"Total Infrastructure Spend: ${total_cost:.2f} USD")
    
    # 3. Error Report
    if oom_pods:
        print(f"Critical Errors (OOMKilled): {', '.join(oom_pods)}")
    else:
        print("Critical Errors: None detected.")
