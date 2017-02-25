def flatten(nested_list):
    flattend_array = []
    for i in nested_list:
        if type(i) is not list:
            flattend_array.append(i)
        else:
            for i in i:
                flattend_array.append(i)
    return flattend_array
