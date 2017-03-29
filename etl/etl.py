def transform(input):
    output = {}
    for key, values in input.items():
        for value in values:
            output[value.lower()] = key
    return output
