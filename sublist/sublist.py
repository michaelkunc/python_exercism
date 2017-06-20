SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def check_lists(first_list, second_list):
    if first_list == second_list:
        return EQUAL
    elif len(second_list) < len(first_list):
        return find_pattern(second_list, first_list, SUPERLIST)

    else:
        return find_pattern(first_list, second_list, SUBLIST)


def find_pattern(small_list, large_list, return_value):
    for i in range(len(large_list) - len(small_list) + 1):
        if small_list == large_list[i:i + len(small_list)]:
            return return_value
    return UNEQUAL
