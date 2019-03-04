from collections import Counter


def score(dice, category):
    return category(dice)


def yacht(dice):
    if len(set(dice)) == 1:
        return 50
    else:
        return 0


def numbers(number):
    return lambda x: sum([i for i in x if i == number])


YACHT = yacht
ONES = numbers(1)
TWOS = numbers(2)
THREES = numbers(3)
FOURS = numbers(4)
FIVES = numbers(5)
SIXES = numbers(6)
FULL_HOUSE = None
FOUR_OF_A_KIND = "four"
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None
