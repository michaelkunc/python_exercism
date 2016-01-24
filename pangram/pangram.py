import string

def is_pangram(sentence):
    sentence = set(sentence.lower().replace(' ',''))
    alphabet = set(string.ascii_lowercase)
    return len(alphabet - sentence) == 0
