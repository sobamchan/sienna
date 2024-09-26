import orjson
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Union


def __get_file_type(fpath: str) -> str:
    if fpath.endswith(".jsonl"):
        return "jsonl"
    elif fpath.endswith(".json"):
        return "json"
    else:
        return "text"


def load(fpath: str | Path) -> Union[List[str], Dict]:
    fpath = str(fpath)

    ftype = __get_file_type(fpath)
    if ftype == "jsonl":
        with open(fpath, "rb") as f:
            data = [orjson.loads(line) for line in f.readlines()]
    elif ftype == "json":
        with open(fpath, "rb") as f:
            data = orjson.loads(f.read())
    else:
        with open(fpath, "r") as f:
            data = [line.strip() for line in f.readlines()]
    return data


def save(
    data: Union[List[Any], Dict], fpath: str | Path, indent: Optional[int] = None
) -> None:
    fpath = str(fpath)

    ftype = __get_file_type(fpath)
    indent = orjson.OPT_INDENT_2 if indent == 2 else None
    if ftype == "jsonl":
        with open(fpath, "wb") as f:
            for d in data:
                f.write(orjson.dumps(d, option=orjson.OPT_APPEND_NEWLINE))
    elif ftype == "json":
        with open(fpath, "wb") as f:
            f.write(orjson.dumps(data, option=indent))
    else:
        with open(fpath, "w") as f:
            f.write("\n".join(data))


def add(data: Dict, fpath: str | Path):
    fpath = str(fpath)

    assert isinstance(
        data, dict
    ), "Currently, only adding dict data to jsonl file is supported."
    assert fpath.endswith(
        ".jsonl"
    ), "Currently, only adding dict data to jsonl file is supported."

    exists = os.path.exists(fpath)

    with open(fpath, "ab") as f:

        if not exists:
            print(f"Creating {fpath}")

        f.write(orjson.dumps(data))
