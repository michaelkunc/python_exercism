def flatten(nested_list):
    flattend_array = []
    return check_type_and_add(nested_list, flattend_array)


def check_type_and_add(nested_list, array):
    for i in nested_list:
        if type(i) is tuple or i is None:
            pass
        elif type(i) is not list:
            array.append(i)
        else:
            check_type_and_add(i, array)
    return array
