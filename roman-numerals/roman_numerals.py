INTEGERS = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
NUMERALS = ('M',  'CM', 'D', 'CD', 'C', 'XC',
            'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')


def numeral(arabic):
    result = []
    for i in range(len(INTEGERS)):
        count = int(arabic / INTEGERS[i])
        result.append(NUMERALS[i] * count)
        arabic -= INTEGERS[i] * count
    return ''.join(result)
