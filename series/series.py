from itertools import permutations

def slices(number, series_length):

    number_list = list(number)
    number_list = [map(int, i) for i in number_list]
    result_list = [number_list[i] for i in range(0, len(number_list), series_length )]
    return result_list