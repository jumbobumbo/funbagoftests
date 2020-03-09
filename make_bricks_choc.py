def make_bricks(small, big, goal):
    """
    big bricks are * 5, small is * 1
    :param small: int
    :param big: int
    :param goal: int
    :return: bool
    """
    total_b = big * 5
    if total_b == goal or small == goal:
        return True
    if total_b + small == goal:
        return True

    if goal - total_b < 0:
        if small >= goal - int(goal // (total_b / big)) * 5:
            return True
        else:
            return False
    elif small >= (goal - total_b):
        return True
    else:
        return False


def make_chocolate(small, big, goal):
    """
    returns -1 if not possible else number of small bars to complete goal
    big bars are * 5, small is * 1
    :param small: int
    :param big: int
    :param goal: int
    :return: int
    """
    if big * 5 == goal:
        return 0
    elif big * 5 > goal:
        max_b = goal // 5
        req_s = goal - (5 * max_b)
        if small < req_s:
            return -1
        else:
            return req_s
    elif big * 5 < goal:
        remaining = goal - (big * 5)
        if small < remaining:
            return -1
        else:
            return remaining


if __name__ == "__main__":
    print(make_bricks(1, 4, 12))
    print(make_chocolate(6, 1, 10))