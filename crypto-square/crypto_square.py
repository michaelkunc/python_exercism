from math import sqrt, ceil


def encode(plaintext):
    normalized = plaintext.lower()
    cols = ceil(sqrt(len(normalized)))
    return ' '.join([normalized[x::cols] for x in range(cols)])
