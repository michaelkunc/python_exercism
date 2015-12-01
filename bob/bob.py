def hey(what):
    what = what.strip()
    response = 'Whatever.'
    if what.isupper():
        response = 'Whoa, chill out!'
    elif not what:
        response = 'Fine. Be that way!'
    elif what.endswith('?'):
        response = 'Sure.'
    return response
