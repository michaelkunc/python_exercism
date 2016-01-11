
digits_to_words = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety"
}

def say(integer):
    response = []
    list_of_ints = [int(l) for l in str(integer)]
    if integer < 21:
        return digits_to_words[integer]
    else:
        tens = list_of_ints[0] * 10
        ones = list_of_ints[-1]
        response.append(digits_to_words[tens])
        response.append(digits_to_words[ones])
        return '-'.join(response)




