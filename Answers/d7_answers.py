# Import and split lines
d7 = open("Data/Day 7 Data.txt", 'r').read().split(',')
d7 = [int(x) for x in d7]
d7e = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def find_triangular_num(num):
    """
    Returns the nth triangular number
    :param num: An integer
    :return: The nth triangular number
    """

    return sum(range(num + 1))


def find_lowest_diff_int(lst):
    """
    Take a list and return the integer which minimises the MAE
    :param lst: List of integers
    :return: The list of integers than minimises the MAE
    """
    # Create a fuel list to record the fuel cost
    fuel = [0] * (max(lst) - min(lst))
    for i in range(max(lst) - min(lst)):
        fuel[i] = sum([abs(x - i) for x in lst])

    return min(fuel)


assert find_lowest_diff_int(d7e) == 37
a1 = find_lowest_diff_int(d7)


def find_lowest_diff_triangle_int(lst) -> int:
    """
    Take a list and return the integer which minimises the difference using triangular numbers
    :param lst: List of integers
    :return: The list of integers than minimises the triangular diff
    """
    # Create a fuel list to record the fuel cost
    fuel = [0] * (max(lst) - min(lst))
    for i in range(max(lst) - min(lst)):
        # Not the most efficient way of coding this...
        fuel[i] = sum([sum(range(abs(x - i) + 1)) for x in lst])

    return min(fuel)


assert find_lowest_diff_triangle_int(d7e) == 168
a2 = find_lowest_diff_triangle_int(d7)
