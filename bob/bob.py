def hey(what):
    what = what.strip()
    if what == what.upper() and any(c.isalpha() for c in what):
        return 'Whoa, chill out!'
    if len(what) == 0:
        return 'Fine. Be that way!'
    if what.endswith('?'):
        return 'Sure.'
    else:
        return 'Whatever.'

