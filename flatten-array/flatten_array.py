def flatten(nested_list):
    flattend_array = []
    x = check_type_and_add(nested_list, flattend_array)
    return x[1]


def check_type_and_add(nested_list, array):
    for i in nested_list:
        if type(i) is not list:
            array.append(i)
        elif len(i) == 0:
            pass
        else:
            check_type_and_add(i, array)
    return (nested_list, array)
