import re


def is_isogram(word):
    word = re.sub(r'\W+', '', word.lower())
    return sorted(list(word)) == sorted(list(set(word)))
