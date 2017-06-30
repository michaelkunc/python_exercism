import math


def primitive_triplets(number):
    results = []
    a, b, c = 1, 3, 0
    while c < number:
        a_ = (a * b) + a
        c = math.sqrt(a_**2 + b**2)
        if c == int(c):
            results.append((b, a_, int(c)))
        a += 1
        b += 1
    return set(results)


def triplets_in_range(number):
    results = []
    a, b, c = 1, 3, 0
    while c < number:
        a_ = (a * b) + a
        c = math.sqrt(a_**2 + b**2)
        if c == int(c):
            results.append((b, a_, int(c)))
        a += 1
        b += 1
    return set(results)


def is_triplet(numbers):
    a, b, c = sorted(numbers)
    return a**2 + b**2 == c**2
