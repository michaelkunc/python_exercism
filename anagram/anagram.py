
def detect_anagrams(word, possible_anagrams):
    return [x for x in possible_anagrams if ''.join(sorted(x.lower())) == ''.join(sorted(word.lower())) and x.lower() != word.lower()]
