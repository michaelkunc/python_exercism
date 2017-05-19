VOWELS = ['a', 'e', 'i', 'o', 'u']
SUFFIX = 'ay'


def translate(text):
    if text[0] in VOWELS:
        text += SUFFIX
    return text
