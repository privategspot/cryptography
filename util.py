def tokenize(message, token_size):
    message_len = len(message)
    return [message[i:i+token_size] for i in range(0, message_len, token_size)]


def pad_with(char: str, subject: str, size: int):
    return subject.ljust(size, char)
