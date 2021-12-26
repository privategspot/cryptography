import logging

from typing import List
from util import tokenize, pad_with


def _permutate(tokens: List[str], key: List[int], key_len: int, reverse: bool = False):
    result = []
    for token in tokens:
        permutation = list(token)
        for i in range(key_len):
            if not reverse:
                permutation[int(key[i] - 1)] = token[i]
                continue
            permutation[i] = token[int(key[i] - 1)]
        result = result + permutation
    return result


def encrypt(message: str, key: List[int]):
    """
    Шифрует сообщение методом блочной перестановки.

    :param str message: Шифротекст
    :param List[int] key: Ключ шифрования блочной перестановки

    :return: Шифротекст message зашифрованный при помощи ключа key
    """
    logging.debug(
        f'start block permutation method encryption with message "{message}" and key "{key}"'
    )

    key_len = len(key)
    tokens = tokenize(message, key_len)

    # если полседний токен меньше, чем длина ключа, то дополняем пробелами
    last_token = tokens[-1]
    if len(last_token) < key_len:
        tokens[-1] = pad_with(" ", last_token, key_len)

    logging.debug(f"message tokens is {tokens}")

    permutation = _permutate(tokens, key, key_len)

    return "".join(permutation)


def decrypt(message, key):
    """
    Дешфирует сообщение, зашифрованное методом блочной перестановки.

    :param str message: Зашифрованный методом блочной перестановки шифротекст
    :param List[int] key: Ключ шифрования блочной перестановки

    :return: Шифротекст message расшифрованный при помощи ключа key
    """
    logging.debug(
        f'start block permutation method decryption with message "{message}" and key "{key}"'
    )

    key_len = len(key)
    tokens = tokenize(message, key_len)

    # если полседний токен меньше, чем длина ключа, то дополняем пробелами
    last_token = tokens[-1]
    if len(last_token) < key_len:
        tokens[-1] = pad_with(" ", last_token, key_len)

    logging.debug(f"message tokens is {tokens}")

    permutation = _permutate(tokens, key, key_len, reverse=True)

    return "".join(permutation).strip()
