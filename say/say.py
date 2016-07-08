
DIGITS_TO_WORDS = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}




def say(integer):
    out_of_range(integer)
    if integer > 20:
        return less_than_101(integer)
    return less_than_21(integer)


def less_than_21(integer):
    return DIGITS_TO_WORDS[integer]

def less_than_101(integer):
    ones = str(integer)[:-1]
    tens = str(integer)[0] + '0'
    return ''.join([DIGITS_TO_WORDS[int(tens)], '-',DIGITS_TO_WORDS[int(ones)]])

def out_of_range(integer):
    if integer < 0:
        raise AttributeError('integer must be greater than 0')
    elif integer >= 1e12:
        raise AttributeError('integer too big!')
