import re


def abbreviate(phrase):
    pattern = r'^\w|(?<=\W)\w|(?<=[a-z])[A-Z]'
    return ''.join([item.upper() for item in re.findall(pattern, phrase)])
