import json
import permutation

from pathlib import Path


with open(Path(__name__).resolve().name + ".json") as f:
    global CASES
    CASES = json.load(f)


def test_encrypt():
    for case in CASES:
        result = permutation.encrypt(case["message"], case["key"])
        assert result == case["permutation"]


def test_decrypt():
    for case in CASES:
        result = permutation.decrypt(case["permutation"], case["key"])
        assert result == case["message"]
