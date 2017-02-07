

def abbreviate(phrase):
    if ':' in phrase:
        phrase = phrase[:phrase.index(':')]
    phrase = phrase.replace('-', ' ')
    letters = [x for ind, x in enumerate(
        phrase) if x == x.upper() or phrase[ind - 1] == ' ']
    return ''.join([i.upper() for i in letters]).replace(' ', '').replace(',', '')
