
def slices(number, series_length):
    if series_length > len(number):
        raise ValueError("Series length must cannot be longer than the length of the number.")
    elif series_length < 1:
        raise ValueError("Series length must be greater than zero.")
    else:
        return [[int(x) for x in number[i:i+series_length]] for i in range(0,len(number) + 1 - series_length)]
