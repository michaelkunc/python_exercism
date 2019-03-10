from collections import Counter


def score(dice, category):
    result = category(dice)
    return result if result else 0


def yacht(dice):
    if len(set(dice)) == 1:
        return 50


def numbers(number):
    return lambda x: sum([i for i in x if i == number])


def full_house(dice):
    item_counts = Counter(dice)
    if set(item_counts.values()) == {2, 3}:
        return sum(dice)


def four_of_a_kind(dice):
    item_counts = Counter(dice)
    if any(i >= 4 for i in item_counts.values()):
        most_common = item_counts.most_common(n=1)[0]
        return most_common[0] * 4


def little_straight(dice):
    if sorted(dice) == [1, 2, 3, 4, 5]:
        return 30


def big_straight(dice):
    if sorted(dice) == [2, 3, 4, 5, 6]:
        return 30


def choice(dice):
    return sum(dice)


YACHT = yacht
ONES = numbers(1)
TWOS = numbers(2)
THREES = numbers(3)
FOURS = numbers(4)
FIVES = numbers(5)
SIXES = numbers(6)
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = little_straight
BIG_STRAIGHT = big_straight
CHOICE = choice
