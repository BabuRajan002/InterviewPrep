import csv
from pathlib import Path
from datetime import datetime, timezone


def stale_files(path: str, days: int, today: str) -> list[str]:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(file_path)
    
    with file_path.open("r", encoding="utf=8",newline='') as log_file:
        log_file_dict = csv.DictReader(log_file)
        dt1 = datetime.strptime(today, "%Y-%m-%dT%H:%M:%SZ")
        result = []
        for row in log_file_dict:
            dt2 = datetime.strptime(row["last_modified_utc"].strip(), "%Y-%m-%dT%H:%M:%SZ")
            diff_days = dt1 - dt2
            if diff_days.days > days:
                result.append(row['filename'])
        return result
                
if __name__ == "__main__":
    current_utc_time = datetime.now(timezone.utc)
    today = current_utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    print(stale_files("/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/1_Basics_Foundation/sample_files/files.csv", 50, today))
