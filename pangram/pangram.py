import string

def is_pangram(sentence):
    sentence = set(sentence.lower().replace(' ',''))
    return len(set(string.ascii_lowercase) - sentence) == 0
