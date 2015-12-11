

def detect_anagrams(word, possible_anagrams):
    results = [x for x in possible_anagrams if ''.join(sorted(x)) == ''.join(sorted(word))]
    return results