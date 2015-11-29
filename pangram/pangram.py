import string


def is_pangram(sentence):
    sentence = sentence.decode('unicode_escape').encode('ascii', 'ignore')
    unique_letters = list(set(''.join(c.lower() for c in sentence  if str.isalpha(c))))
    if len(unique_letters) == 26:
        return True
    else:
        return False
