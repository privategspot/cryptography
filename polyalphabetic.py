from typing import List
from util import tokenize, pad_with


def _permutate(token: str, key: List[List[str]], key_len: int) -> List[str]:
    permutation = list(token)
    for i in range(len(permutation)):
        current_char = permutation[i]
        replace_alphabet = key[i % key_len]
        if current_char in replace_alphabet:
            replace_char = replace_alphabet[(replace_alphabet.index(current_char) + 1) % key_len]
            permutation[i] = replace_char

    return permutation


def encrypt(message: str, key: List[List[str]]) -> str:
    """
    Шифрует сообщение многоалфавитным шифром.

    :param str message: Шифротекст
    :param List[List[str]] key: Ключ шифрования многоалфавитного шифра

    :return: Шифротекст message зашифрованный при помощи ключа key
    """
    alphabets_num = len(key)
    tokens = tokenize(message, alphabets_num)

    last_token = tokens[-1]
    if len(last_token) < alphabets_num:
        tokens[-1] = pad_with(" ", last_token, alphabets_num)

    result = []
    for i in range(len(tokens)):
        result = result + _permutate(tokens[i], key, alphabets_num)

    return "".join(result)


def decrypt(message: str, key: List[str]) -> str:
    """
    Дешфирует сообщение, зашифрованное многоалфавитным шифром.

    :param str message: Зашифрованный многоалфавитным шифром шифротекст
    :param List[int] key: Ключ шифрования многоалфавитного шифра

    :return: Шифротекст message расшифрованный при помощи ключа key
    """
    alphabets_num = len(key)
    tokens = tokenize(message, alphabets_num)

    last_token = tokens[-1]
    if len(last_token) < alphabets_num:
        tokens[-1] = pad_with(" ", last_token, alphabets_num)

    result = []
    for i in range(len(tokens)):
        result = result + _permutate(tokens[i], key, alphabets_num)

    return "".join(result)
