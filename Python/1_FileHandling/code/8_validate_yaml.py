import yaml
from pathlib import Path

def validate_yaml(path: str) -> None:
    file_path = Path(path)

    if not file_path.exists():
        print(f"File not found {file_path}")
        return
    
    with file_path.open('r', encoding="utf=8") as fy:
        content = yaml.safe_load(fy)
        lst = content["required_keys"]
        print(lst)
        for value in content.values():            
            for val in value:
              print(val)


                

if __name__ == "__main__":
    validate_yaml("/Users/babus/Desktop/repos/InterviewPrep/Python/1_FileHandling/sample_files/validate_yaml.yaml")