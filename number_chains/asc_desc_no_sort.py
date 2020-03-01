class ReorderInt:
    def __init__(self, number, ascending=True):
        """
        Reorders an int into ascending or descending order
        :param number: int
        :param ascending: bool
        return: int
        """
        self.number = list(str(number))
        self.ascending = ascending
        self.result = self.list_to_int(self.sort_list())

    def sort_list(self):
        """
        :return: list
        """
        return_list = []
        while self.number:
            compare_val = self.number[0]  # first element in list
            for x in self.number:
                if self.ascending:
                    if int(x) < int(compare_val):
                        compare_val = x
                else:
                    if int(x) > int(compare_val):
                        compare_val = x
            return_list.append(compare_val)
            self.number.remove(compare_val)
        return return_list

    @staticmethod
    def list_to_int(listn):
        """
        :param listn: list
        :return:  int
        """
        return int("".join(x for x in listn))


#num = list(str(3432432413))
#sorted_num = list_to_int(sort_list(num))

