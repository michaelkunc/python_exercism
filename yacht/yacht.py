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


def full_house(dice):
    item_counts = Counter(dice)
    if set(item_counts.values()) == {2, 3}:
        return sum(dice)
    else:
        return 0


def four_of_a_kind(dice):
    item_counts = Counter(dice)
    if any(i >= 4 for i in item_counts.values()):
        most_common = item_counts.most_common(n=1)[0]
        return most_common[0] * 4
    else:
        return 0


YACHT = yacht
ONES = numbers(1)
TWOS = numbers(2)
THREES = numbers(3)
FOURS = numbers(4)
FIVES = numbers(5)
SIXES = numbers(6)
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None
