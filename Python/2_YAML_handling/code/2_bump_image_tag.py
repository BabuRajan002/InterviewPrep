from ruamel.yaml import YAML
from pathlib import Path

yaml = YAML(typ="rt")       # round-trip mode: preserve formatting & comments
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.width = 4096
yaml.preserve_quotes = True
# yaml.explicit_start = True

path = Path("/Users/babus/Desktop/repos/InterviewPrep/Python/2_YAML_handling/sample_files/manifests.yaml")

# Load all docs
with path.open(encoding="utf=8") as f:
    docs = list(yaml.load_all(f))

# Modify in place
for d in docs:
    containers = d.get("spec", {}).get("template", {}).get("spec", {}).get("containers", [])
    for c in containers:
        img = c.get("image")
        if img and "ghcr.io/acme/" in img:
            # strip any old tag and force :latest
            base = img.split("@", 1)[0]  # remove digest if any
            last_colon = base.rfind(":")
            last_slash = base.rfind("/")
            print(last_colon,last_slash)
            if last_colon > last_slash:   # only strip if colon is after last slash
                base = base[:last_colon]
                
            c["image"] = f"{base}:latest"

# Write back to original file
with path.open("w", encoding="utf=8") as f:
    yaml.dump_all(docs, f)
