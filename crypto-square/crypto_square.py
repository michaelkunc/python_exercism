import math


def encode(plaintext):
    normalized = plaintext.lower()
    columns = math.sqrt(len(normalized))
    cipher_text = normalized
    return cipher_text
