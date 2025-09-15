from pathlib import Path
import json

def extract_failed_pods(path: str) -> None:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(file_path)
    
    with file_path.open('r', encoding='utf-8') as f:
        k8s_state = json.load(f)
        failed_pods = []
        for item in k8s_state['items']:
            if item['status']['phase'] != 'Running':
                failed_pods.append(item['metadata']['name'])
        print(f"Failed pods: {failed_pods}")


if __name__ == "__main__":
    extract_failed_pods("/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/1_Basics_Foundation/sample_files/failed_pods.json")