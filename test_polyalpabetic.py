import json
import polyalphabetic

from pathlib import Path


with open(Path(__name__).resolve().name + ".json") as f:
    global CASES
    CASES = json.load(f)


def test_encrypt():
    for case in CASES:
        result = polyalphabetic.encrypt(case["message"], case["key"])
        assert result == case["encrypted"]


def test_decrypt():
    for case in CASES:
        result = polyalphabetic.decrypt(case["encrypted"], case["key"])
        assert result == case["message"]
