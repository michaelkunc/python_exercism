from collections import Counter

# Score categories
# Change the values as you see fit
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None


def score(dice, category):
    item_counts = Counter(dice)
    if item_counts.most_common(n=1)[0][1] == 5 and category is YACHT:
        return YACHT
    if category == FULL_HOUSE:
        if set(item_counts.values()) == {2, 3}:
            return sum(dice)
        else:
            return 0
    else:
        return item_counts[category] * category
