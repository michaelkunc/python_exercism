import math

def sieve(upper_limit):
    return [x for x in range(2,upper_limit + 1) if is_prime(x)]

def is_prime(number):
    if number % 2 == 0 and number > 2:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

