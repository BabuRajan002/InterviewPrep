import json
from pathlib import Path
import sys

def missing_field(path: str) -> None:
    file_path = Path(path)

    with file_path.open('r', encoding='utf-8') as f:
        k8s_file = json.load(f)
        original_keys = ['name', 'image', 'replicas']
        has_issues = False
        for service in k8s_file['services']:
            keys_list = service.keys()
            missing_keys = list(set(original_keys) - set(keys_list))
            if missing_keys:
                print(f"{service['name']} -> missing: {', '.join(missing_keys)}") 

        if has_issues:
          sys.exit(1)

        


if __name__ == "__main__":
    missing_field("/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/1_Basics_Foundation/sample_files/k8s.json")