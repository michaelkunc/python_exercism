
def is_pangram(sentence):
    sentence = sentence.decode('unicode_escape').encode('ascii', 'ignore')
    return len(set([c for c in sentence.lower() if str.isalpha(c)])) == 26
