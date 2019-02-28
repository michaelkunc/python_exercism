# Score categories
# Change the values as you see fit
from collections import Counter
from functools import reduce
import operator

YACHT = 50
ONES = 1
TWOS = None
THREES = None
FOURS = None
FIVES = None
SIXES = None
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None


def score(dice, category):
    dice_set = set(dice)
    unique_items = len(dice_set)
    item_counts = Counter(dice)
    most_common = item_counts.most_common(n=1)[0]
    most_common_element = most_common[0]
    if unique_items == 1 and category is YACHT:
        return YACHT
    if unique_items > 1 and category == most_common_element:
        return reduce(operator.mul, most_common)
    return 0
