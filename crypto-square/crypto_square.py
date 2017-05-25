from math import sqrt, ceil


def encode(plain):
    normalized = ''.join([c for c in plain.lower() if c.isalnum()])
    cols = ceil(sqrt(len(normalized)))
    return ' '.join([normalized[x::cols] for x in range(cols)])
