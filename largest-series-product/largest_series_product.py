def largest_product(integer_string, digits):
    integers = [int(i) for i in integer_string]
    return max([reduce((lambda x, y: x * y), list(integers[i:i + digits])) for i in range(0, len(integers) - 1)])
