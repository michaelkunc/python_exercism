VOWELS = ['a', 'e', 'i', 'o', 'u']
PREFIXES = ['yt', 'xr']


def translate(phrase):
    results = []
    for word in phrase.split(' '):
        if word[0] in VOWELS or word[:2] in PREFIXES:
            pass
        elif 'qu' in word:
            word = vowel_after_qu(word)
        else:
            word = find_first_vowel(word)
        results.append(word + 'ay')
    return ' '.join(results)


def find_first_vowel(word):
    for index, char in enumerate(word):
        if char in VOWELS:
            vowel_ix = index
            break
    return word[vowel_ix:] + word[:vowel_ix]


def vowel_after_qu(word):
    vowel_ix = word.index('qu') + 2
    return word[vowel_ix:] + word[:vowel_ix]
