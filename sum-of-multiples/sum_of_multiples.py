
def sum_of_multiples(upper_limit, multiples=[]):
    if multiples:
        return sum(x for x in list(range(1, upper_limit)) if is_multiple(x, multiples))
    else:
        return sum(x for x in list(range(1, upper_limit)) if x % 3 == 0 or x % 5 == 0)


def is_multiple(number, multiples=[]):
    return len([i for i in multiples if number % i == 0]) > 0


