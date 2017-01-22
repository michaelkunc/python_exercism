from string import lowercase

def is_pangram(sentence):
    sentence = set(sentence.lower().replace(' ',''))
    return len(set(lowercase) - sentence) == 0
