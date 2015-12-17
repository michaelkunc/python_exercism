
def detect_anagrams(word, possible_anagrams):
    return [x for x in possible_anagrams if is_anagram(word, x)]

def is_anagram(first_word, second_word):
    first_word = first_word.lower()
    second_word = second_word.lower()
    return first_word != second_word and sorted(first_word) == sorted(second_word)
