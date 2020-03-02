
class CalcStatList:
    def __init__(self, listn: list):
        self.listn = listn

    def _find_val(self, min_val: bool = True) -> int:
        """
        finds min or max val of list, controlled be min_val
        :param min_val: bool
        :return: int
        """
        sorted_list = sorted(self.listn, reverse=min_val)
        return sorted_list[-1]

    def _list_len(self) -> int:
        """
        returns len of list
        :return: int
        """
        return len(self.listn)

    def _list_avg_val(self) -> float:
        """
        returns average value of list
        :return: float
        """
        total_val = 0
        for i in self.listn:
            total_val += i
        return total_val / self._list_len()

    def return_stats(self) -> str:
        """
        returns all above stats for list
        :return: str
        """
        return f"minimum value: {self._find_val(True)} \n" \
               f"maximum value: {self._find_val(False)} \n" \
               f"number of elements in the sequence: {self._list_len()} \n" \
               f"average value: {self._list_avg_val()}"


if __name__ == "__main__":
    print(CalcStatList([2, 5, 7, 44, 88, 1, 2, -2, 6]).return_stats())
