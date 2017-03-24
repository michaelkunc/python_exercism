import re


def is_isogram(word):
    word = re.sub(r'\W+', '', word.lower())
    return len(word) == len(set(word))
