import math


def primitive_triplets(number):
    if number % 2 != 0:
        raise ValueError
    else:
        results = set()
        for (m, n) in _get_factors(number // 2):
            if math.gcd(m, n) == 1:
                triplet = tuple(sorted((m**2 - n**2, 2 * m * n, m**2 + n**2)))
                results.add(triplet)
        return results


def _get_factors(n):
    return ((n // i, i) for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)


def triplets_in_range(start, end):
    end = end + 1
    results = set()
    for a in range(start, end):
        for b in range(a + 1, end):
            for c in range(b + 1, end):
                if a * a + b * b == c * c:
                    results.add((a, b, c))
    return results


def is_triplet(numbers):
    a, b, c = sorted(numbers)
    return a**2 + b**2 == c**2
