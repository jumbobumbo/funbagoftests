
def sort_list(listn, ascending=True):
    """
    defaults to ascending, else descending
    :param listn: list
    :param ascending: bool
    :return: list
    """
    return_list = []
    while listn:
        compare_val = listn[0]  # first element in list
        for x in listn:
            if ascending:
                if int(x) < int(compare_val):
                    compare_val = x
            else:
                if int(x) > int(compare_val):
                    compare_val = x
        return_list.append(compare_val)
        listn.remove(compare_val)
    return return_list


def list_to_int(listn):
    """
    feed it a list, returns an int (of the list items in order)
    :param listn: list
    :return: int
    """
    return int("".join(x for x in listn))


num = list(str(3432432413))
sorted_num = list_to_int(sort_list(num))
print(sorted_num)
