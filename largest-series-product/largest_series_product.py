def largest_product(integer_string, digits):
    integers = sorted([int(i) for i in integer_string])
    return reduce(lambda x, y: x * y, integers[-digits:])
