import json
import os
from typing import Any, Dict, List, Optional, Union


def __get_file_type(fpath: str) -> str:
    if fpath.endswith(".jsonl"):
        return "jsonl"
    elif fpath.endswith(".json"):
        return "json"
    else:
        return "text"


def load(fpath: str) -> Union[List[str], Dict]:
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


def save(
    data: Union[List[Any], Dict], fpath: str, indent: Optional[int] = None
) -> None:
    ftype = __get_file_type(fpath)
    if ftype == "jsonl":
        with open(fpath, "w") as f:
            f.write("\n".join([json.dumps(d) for d in data]))
    elif ftype == "json":
        with open(fpath, "w") as f:
            json.dump(data, f, indent=indent)
    else:
        with open(fpath, "w") as f:
            f.write("\n".join(data))


def add(data: Dict, fpath: str):
    assert isinstance(
        data, dict
    ), "Currently, only adding dict data to jsonl file is supported."
    assert fpath.endswith(
        ".jsonl"
    ), "Currently, only adding dict data to jsonl file is supported."

    exists = os.path.exists(fpath)

    with open(fpath, "a") as f:

        if exists:
            f.write("\n")
        else:
            print(f"Creating {fpath}")

        f.write(json.dumps(data))
