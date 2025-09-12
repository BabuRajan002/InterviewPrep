from pathlib import Path
import re
def extract_error_codes(path: str) -> list[str]:
    file_path = Path(path)

    with file_path.open('r', encoding="utf-8") as error_file:
        for line in error_file:
             line = line.strip()

           






if __name__ == "__main__":
    extract_error_codes("/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/1_Basics_Foundation/sample_files/distinct_error_code.log")
  