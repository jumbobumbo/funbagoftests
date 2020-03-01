

def remove_duplicate_elem_from_lst(list1):
    """
    removes duplicate elements, returns amended list
    :param list1: list
    :return: list
    """
    wanted_elements = []
    for elem in list1:
        if elem not in wanted_elements:
            wanted_elements.append(elem)
    return wanted_elements


def remove_duplicate_elems_from_lst_with_dict(list1):
    """
    utilises dict.fromkeys to be a lil cheeky (dict keys cannot have duplicates - does the job for us :O)
    :param list1: list
    :return: list
    """
    return list(dict.fromkeys(list1))
