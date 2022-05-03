import json
from typing import Dict, List, Union


def __get_file_type(fpath: str) -> str:
    if fpath.endswith(".jsonl"):
        return "jsonl"
    elif fpath.endswith(".json"):
        return "jsonl"
    else:
        return "text"


def load(fpath: str) -> Union[List, Dict]:
    ftype = __get_file_type(fpath)
    if ftype == "jsonl":
        with open(fpath, "r") as f:
            data = [json.loads(line) for line in f.readlines()]
    elif ftype == "json":
        with open(fpath, "r") as f:
            data = json.load(f)
    else:
        with open(fpath, "r") as f:
            data = [line.strip() for line in f.readlines()]
    return data


def save(data: Union[List, Dict], fpath: str) -> None:
    ftype = __get_file_type(fpath)
    if ftype == "jsonl":
        with open(fpath, "w") as f:
            f.write("\n".join([json.dumps(d) for d in data]))
    elif ftype == "json":
        with open(fpath, "w") as f:
            json.dump(data, f)
    else:
        with open(fpath, "w") as f:
            f.write("\n".join(data))
