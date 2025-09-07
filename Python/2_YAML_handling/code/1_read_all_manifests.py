import yaml
docs = list(yaml.safe_load_all(open("/Users/babus/Desktop/repos/InterviewPrep/Python/2_YAML_handling/sample_files/manifests.yaml", "r", encoding="utf-8")))
for d in docs:
    print(d["kind"])