from collections import defaultdict


def word_count(words):
    word_count = defaultdict(int)
    for word in words.lower().split():
        word_count[word] += 1
    return word_count
