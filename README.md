SIENNA (SImplE jsoN liNe pArser)


This only saves 1 lines of code, to load/save jsonl files.

## Installation

```bash
> pip install sienna
```


## Usage

Loading.

```py
# BEFORE
import json
with open(fpath, "r") as f:
    data = [json.loads(line) for line in f.readlines()]

# With sienna
import sienna
data = sienna.load(fpath)
```

Saving.

```py
# BEFORE
import json
with open(fpath, "w") as f:
    f.write("\n".join([json.dumps(d) for d in data]))

# With sienna
import sienna
data = sienna.save(data, fpath)
```

## Other file types

Now sienna supports following file types,

- jsonline files (`hoge.jsonl`),
- json files (`hoge.json`),
- `\n` separated text files (`hoge.[anything but not jsonl and json]`).

sienna checks file extension and read differently.
