import json
import sys

import yaml

yaml_file_path = sys.argv[1]
json_file_path = sys.argv[2]


def correct_ref(d: dict):
    for k, v in d.items():
        if k == "$ref" and isinstance(v, str):
            v_parts = v.split(".")
            if v_parts[-1] == "yaml":
                v_parts[-1] = "json"
                d[k] = ".".join(v_parts)
        elif isinstance(v, dict):
            correct_ref(v)
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    correct_ref(item)


with open(yaml_file_path) as f:
    data = yaml.safe_load(f)
    correct_ref(data)

with open(json_file_path, "w+") as f:
    json.dump(data, f, indent=2)
