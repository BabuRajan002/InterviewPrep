import yaml
from ruamel.yaml import YAML
yaml = YAML(typ="rt")
yaml.indent(mapping=2, sequence=2, offset=2)

# with open("/Users/babus/Desktop/repos/InterviewPrep/Python/2_YAML_handling/sample_files/manifests.yaml", encoding="utf=8") as f:
#     doc = list(yaml.safe(f))

docs = list(yaml.safe_load_all(open("/Users/babus/Desktop/repos/InterviewPrep/Python/2_YAML_handling/sample_files/manifests.yaml", "r", encoding="utf-8")))

for d in docs:
# if doc["spec"]["template"]["spec"]["containers"][0]["image"] == ""
 print(d["spec"]["template"]["spec"]["containers"][0]["image"])
   



