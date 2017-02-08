import re


def abbreviate(phrase):
    return ''.join([item[0].upper() for item in re.findall(r'\S+', phrase)])
