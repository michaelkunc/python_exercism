import string

def is_pangram(sentence):
    sentence = sentence.decode('unicode_escape').encode('ascii', 'ignore').lower()
    alphabet = string.ascii_lowercase
    return len(set(alphabet) - set(sentence.replace(" ",""))) == 0
