import subprocess
from pathlib import Path

def subprocess_testing(command: str, file_path: str):
    r = subprocess.run(f"{command} {file_path}", capture_output=True, text=True, shell=True)
    return r.stdout.strip(), r.stderr.strip(), r.returncode

if __name__ == "__main__":
    stdout, stderr, code = subprocess_testing("ls -l", "/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/2_file_os_automation/code/source_dir/")
    print("Exit Code: ", code)
    print("STDOUT:", stdout)
    print("STDERR:", stderr)