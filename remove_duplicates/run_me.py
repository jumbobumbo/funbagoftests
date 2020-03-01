from remove_duplicates import remove_duplicate_elem_from_lst

lists = [[1, 2, 3, 4, 5, 6, 44, 44, 1, 3, 5, 9, 9, 9, 9],
         [1],
         [],
         [2, 4, 5, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8]]


for list_n in lists:
    print(remove_duplicate_elem_from_lst(list_n))
