from typing import List


class LinearRandGenerator:
    """
    Линейный конгруэнтный генератор ПСЧ
    """

    def __init__(self, seed, machine_word_len=6, A=5, C=3):
        self._A = A
        self._C = C
        self._M = 2 ** machine_word_len
        self._seed = seed

    def rand(self):
        """
        Генерирует ПСЧ
        """
        res = (self._A * self._seed + self._C) % self._M
        self._seed = res
        return res


def generate_key(key_len: int, seed: int):
    lrg = LinearRandGenerator(seed)

    res = []
    for _ in range(key_len):
        res.append(lrg.rand())

    return res


def _xor_method(message: str, key: List[int]):
    res = []
    for i in range(len(message)):
        res.append(chr(ord(message[i]) ^ key[i]))

    return "".join(res)


def encrypt(message: str, key: List[int]):
    """
    Зашифровывает шифротекст message XOR методом используя ключ key.

    :param str message: Шифротекст
    :param List[int] key: Ключ

    :return: Зашифрованный шифротекст
    """
    return _xor_method(message, key)


def decrypt(message: str, key: List[int]):
    """
    Расшифровывает шифротекст message XOR методом используя ключ key.

    :param str message: Шифротекст
    :param List[int] key: Ключ

    :return: Расшифрованный шифротекст
    """
    return _xor_method(message, key)
