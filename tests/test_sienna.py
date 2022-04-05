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
