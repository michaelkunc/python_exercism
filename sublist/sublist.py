
def SUBLIST():
    pass


def SUPERLIST():
    pass


def EQUAL():
    pass


def UNEQUAL():
    pass


def check_lists(first_list, second_list):
    if first_list == second_list:
        return EQUAL
    elif len(first_list) == 0:
        return SUBLIST
    else:
        return SUPERLIST
