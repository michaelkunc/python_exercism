import itertools

def slices(number, series_length):

    # number_list = list(number)
    # number_list = [map(int, i) for i in number_list]
    # result_list = [number_list[i] for i in range(0, len(number_list), series_length )]
    # return result_list

    results = []
    number_list = list(number)
    number_list = [int(i) for i in number_list]
    combinations = itertools.combinations(number_list, series_length)
    combinations = [list(i) for i in combinations]
    for i in combinations:
        if i not in results:
            results.append(i)
    return results