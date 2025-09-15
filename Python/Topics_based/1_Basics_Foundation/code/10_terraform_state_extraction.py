from pathlib import Path
import json

def terraform_instace_state_details(path: str) -> None:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(file_path)

    with file_path.open('r', encoding='utf-8') as f:
        tf = json.load(f)
        
        rows = []
        for resource in tf.get("resources", []):
            resource_type = resource.get("type", "<Unknown>")
            if resource_type == "google_compute_instance":
                inst_name = resource.get("name", "<unknown>")
                inst_zone = resource.get("instances", [])
                for zone in inst_zone:
                    zone_name = zone.get("attributes", "<Unknown>").get("zone", "<Unknown>")
                rows.append((inst_name, zone_name))
        rows.sort(key=lambda x: (x[0], x[1]))

   
    with open('/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/1_Basics_Foundation/sample_files/instances.tsv', 'w', encoding='utf-8') as wf:
        for name, zone in rows:
          wf.write(f"{name}\t{zone}\n")
        
    

if __name__ == "__main__":
    terraform_instace_state_details("/Users/babus/Desktop/repos/InterviewPrep/Python/Topics_based/1_Basics_Foundation/sample_files/terraform_state.json")