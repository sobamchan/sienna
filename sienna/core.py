import json
from typing import Dict, List, Union


def load(fpath: str) -> Union[List, Dict]:
    with open(fpath, "r") as f:
        data = [json.loads(line) for line in f.readlines()]
    return data


def save(data: Union[List, Dict], fpath: str) -> None:
    with open(fpath, "w") as f:
        f.write("\n".join([json.dumps(d) for d in data]))
