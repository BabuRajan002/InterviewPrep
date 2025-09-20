import os
import glob

direct_path = "."

def list_log_files(base_dir: str = "."):
    return glob.glob(os.path.join(base_dir, "*.log"))

def list_log_files_recursively(base_dir: str = "."):
    logs = []

    for root, _, files in os.walk(base_dir):
        for f in files:
            if f.endswith(".log"):
                logs.append(os.path.join(root, f))
    return logs


if __name__ == "__main__":
    print(f"non recursive output: ", list_log_files("."))
    print(f"recursive output:", list_log_files_recursively("."))




