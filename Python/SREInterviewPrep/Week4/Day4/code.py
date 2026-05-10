import os
import time 

def get_process_metrics(pid):
    status_path = f"/proc/{pid}/staus"

    try: 
        with open(status_path, 'r') as f:
            for line in f:
                if line.startswith("VmRSS:"):
                    parts = line.split()
                    mem_kb = int(parts[1])
                    return mem_kb / 1024
    except FileNotFoundError:
        return None

def monitor_process(pid, threshold_mb=500):
    print(f"monitoring PID {pid} (Threshold: {threshold_mb})....")

    try: 
        while True:
            mem_usage = get_process_metrics(pid)
            if mem_usage is None:
                print(f"ALERT : Process ID {pid} has been terminated")
                break             
            if mem_usage > threshold_mb:
                print(f"CRITICAL: PID {pid} using {mem_usage:.2f}MB - Exceeds Threshold!")            
            else:
                print(f"INFO: PID {pid} usage: {mem_usage:.2f}MB (Normal)")
            
            time.sleep(5)
    
    except KeyboardInterrupt:
        print("\n Moniroting Stopped")

if __name__ == "__main__":
    current_pid = os.getpid()
    monitor_process(current_pid, threshold_mb=100)


