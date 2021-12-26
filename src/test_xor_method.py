import json
import time
import xor_method

from pathlib import Path


with open(Path(__name__).resolve().name + ".json") as f:
    global CASES
    CASES = json.load(f)


def test_xor_method():
    for case in CASES:
        key_len = len(case)
        seed = int(time.time())
        key = xor_method.generate_key(key_len, xor_method.LinearRandGenerator, seed)
        enc_res = xor_method.encrypt(case, key)
        dec_res = xor_method.decrypt(enc_res, key)
        assert dec_res == case


def test_xor_method_with_feedback():
    for case in CASES:
        key_len = len(case)
        seed = int(time.time())
        key = xor_method.generate_key(key_len, xor_method.LinearRandGeneratorWithFeedback, seed)
        enc_res = xor_method.encrypt(case, key)
        dec_res = xor_method.decrypt(enc_res, key)
        assert dec_res == case