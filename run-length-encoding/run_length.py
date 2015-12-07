from itertools import groupby
from re import sub


def encode(string):
    compress = lambda x: str(len(x.group(0))) + x.group(0)[0]
    return sub(r'(.)\1+', compress, string)


def decode(string):
    decompress = lambda x: x.group(2) * int(x.group(1))
    return sub(r'(\d+)(\D)', decompress, string)
