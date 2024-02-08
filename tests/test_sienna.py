import sienna
from sienna import __version__


def test_version():
    assert __version__ == "0.1.1"


def test_load():
    data = sienna.load("./tests/test_data.jsonl")
    assert data == [
        {
            "city": "tokyo",
            "country": "japan",
        },
        {
            "city": "mannheim",
            "country": "germany",
        },
    ]


def test_save_jsonl():
    temp_path = "/tmp/test.jsonl"
    data = [
        {
            "city": "tokyo",
            "country": "japan",
        },
        {
            "city": "mannheim",
            "country": "germany",
        },
    ]
    sienna.save(data, temp_path)
    loaded_data = sienna.load(temp_path)
    assert data == loaded_data


def test_save_json():
    temp_path = "/tmp/test.json"
    data = {
        "city": "mannheim",
        "country": "germany",
    }
    sienna.save(data, temp_path)
    loaded_data = sienna.load(temp_path)
    assert data == loaded_data   


def test_add():
    temp_path = "/tmp/test.jsonl"
    data = [
        {
            "city": "tokyo",
            "country": "japan",
        },
        {
            "city": "mannheim",
            "country": "germany",
        },
    ]
    sienna.save(data, temp_path)
    new_data = {
        "city": "tbilisi",
        "country": "georgia",
    }
    sienna.add(new_data, temp_path)
    loaded_data = sienna.load(temp_path)
    assert loaded_data == data + [new_data]
