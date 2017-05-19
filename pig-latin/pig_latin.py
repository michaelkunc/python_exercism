
def translate(english):
    return ' '.join([translate_words(word) for word in english.split()])


def translate_words(word):
    vowels = set(['a', 'e', 'i', 'o'])
    for index, char in enumerate(word):
        if char in vowels or char in set(['u', 'y', 'x']) and word[index + 1] not in vowels:
            return word[index:] + word[:index] + 'ay'
