
DIGITS_TO_WORDS = {
    '0': "zero",
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "five",
    '6': "six",
    '7': "seven",
    '8': "eight",
    '9': "nine",
    '10': "ten",
    '11': "eleven",
    '12': "twelve",
    '13': "thirteen",
    '14': "fourteen",
    '15': "fifteen",
    '16': "sixteen",
    '17': "seventeen",
    '18': "eighteen",
    '19': "nineteen",
    '20': "twenty",
    '30': "thirty",
    '40': "forty",
    '50': "fifty",
    '60': "sixty",
    '70': "seventy",
    '80': "eighty",
    '90': "ninety"
}

MAGNITUDES = ['hundred', 'thousand', 'million', 'billion']


def say(integer):
    integer = int(integer)
    out_of_range(integer)
    if integer > 9999999:
        split_integer = divy_into_hundreds(str(integer))
        if set(split_integer[1:]) == {'000'}:
            return ''.join([less_than_21(split_integer[0]),' ',MAGNITUDES[3]])
        else:
            return ''.join([handle_the_hundreds(split_integer[0]),' ',MAGNITUDES[3],' ',handle_the_hundreds(split_integer[1]),' ',MAGNITUDES[2],' ',handle_the_hundreds(split_integer[2]),' ',MAGNITUDES[1],' ',handle_the_hundreds(split_integer[3])])
    elif integer > 999999:
        split_integer = divy_into_hundreds(str(integer))
        if set(split_integer[1:]) == {'000'}:
            return ''.join([less_than_21(split_integer[0]), ' ', MAGNITUDES[2]])
        elif split_integer[1] == '000':
            return ''.join([less_than_21(split_integer[0]), ' ', MAGNITUDES[2], ' and ', less_than_21(str(int(split_integer[2])))])
        else:
            return ''.join([less_than_21(split_integer[0]), ' ', MAGNITUDES[2], ' ', less_than_21(str(int(split_integer[1]))), ' ', MAGNITUDES[1], ' ', handle_the_hundreds(split_integer[2])])
    elif integer > 999:
        split_integer = divy_into_hundreds(str(integer))
        if set(split_integer[1:]) == {'000'}:
            return ''.join([less_than_21(split_integer[0]), ' ', MAGNITUDES[1]])
        else:
            return ''.join([less_than_21(split_integer[0]), ' ', MAGNITUDES[1], ' ', handle_the_hundreds(split_integer[1])])
    elif integer > 99:
        return handle_the_hundreds(str(integer))
    elif integer > 20:
        return less_than_100(str(integer))
    else:
        return less_than_21(str(integer))


def less_than_21(integer):
    return DIGITS_TO_WORDS[integer]


def less_than_100(integer):
    return DIGITS_TO_WORDS[integer[0] + '0'] + '-' + DIGITS_TO_WORDS[integer[1]]


def less_than_1000(integer):
    return DIGITS_TO_WORDS[integer[0]] + ' ' + MAGNITUDES[0]


def handle_the_hundreds(integer):
    result = []
    result.append(less_than_1000(integer))
    integer = int(integer[1:])
    if integer > 0 and integer < 21:
        result.append(' and ' + less_than_21(str(integer)))
    elif integer > 0:
        result.append(' and ' + less_than_100(str(integer)))
    return ''.join(result)


def divy_into_hundreds(integer):
    leading_digits = len(integer) % 3
    if leading_digits == 0:
        return split_remaining_digits(integer)
    else:
        return split_leading_digits(integer, leading_digits) + split_remaining_digits(integer[leading_digits:])


def split_leading_digits(integer, leading_digits):
    return [integer[0:leading_digits]]


def split_remaining_digits(integer):
    return [integer[i:i + 3] for i in range(0, len(integer), 3)]


def out_of_range(integer):
    if integer < 0:
        raise AttributeError('integer must be greater than 0')
    elif integer >= 1e12:
        raise AttributeError('integer too big!')
