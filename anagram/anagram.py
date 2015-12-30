
def detect_anagrams(word, possible_anagrams):
    word = word.lower()
    return filter(lambda x: sorted(x.lower()) == sorted(word) and x.lower() != word, possible_anagrams)

