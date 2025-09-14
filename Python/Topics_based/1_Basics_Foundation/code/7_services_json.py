from pathlib import Path
import json

def read_services(path: str) -> None:
    file_path = Path(path)
    
    if not file_path.exists():
        raise FileNotFoundError(file_path)
    
    with file_path.open('r', encoding="utf-8") as service_file:
        f = json.load(service_file)

    for service in f['services']:
        if "replicas" not in service:
            service['replicas'] = 1
        
            
    with open('/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/1_Basics_Foundation/sample_files/services_fixed.json', 'w', encoding='utf-8') as f:
        json.dump(service, f, indent=2)
    


if __name__ == "__main__":
   read_services("/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/1_Basics_Foundation/sample_files/services.json")
