d9 = open("Data/Day 9 Data.txt", 'r').read().split("\n")
d9e = ['2199943210',
       '3987894921',
       '9856789892',
       '8767896789',
       '9899965678',
       ]

from collections import Counter
from numpy import prod


def get_adj_peaks(num_grid, x, y):
    """
    Get all the adjacent points for a point x,y in a number grid
    :param num_grid: Grid of numbers in list form
    :param x: x co-ordinate
    :param y: y co-ordinate
    :return: Numers of adjacent peaks, co-ordinates of adjacent peaks
    """
    if x == 0:
        # a is a list of all adjacent numbers
        # b is a list of all adjacent co-ordinates
        if y == 0:
            a = [num_grid[x + 1][y], num_grid[x][y + 1]]
            b = [(x + 1, y), (x, y + 1)]
        elif y == (len(num_grid[0]) - 1):
            a = [num_grid[x + 1][y], num_grid[x][y - 1]]
            b = [(x + 1, y), (x, y - 1)]
        else:
            a = [num_grid[x + 1][y], num_grid[x][y + 1], num_grid[x][y - 1]]
            b = [(x + 1, y), (x, y - 1), (x, y + 1)]
    elif x == (len(num_grid) - 1):
        if y == 0:
            a = [num_grid[x - 1][y], num_grid[x][y + 1]]
            b = [(x - 1, y), (x, y + 1)]
        elif y == (len(num_grid[0]) - 1):
            a = [num_grid[x - 1][y], num_grid[x][y - 1]]
            b = [(x - 1, y), (x, y - 1)]
        else:
            a = [num_grid[x - 1][y], num_grid[x][y + 1], num_grid[x][y - 1]]
            b = [(x - 1, y), (x, y + 1), (x, y - 1)]
    else:
        if y == 0:
            a = [num_grid[x - 1][y], num_grid[x + 1][y], num_grid[x][y + 1]]
            b = [(x - 1, y), (x, y + 1), (x + 1, y)]
        elif y == (len(num_grid[0]) - 1):
            a = [num_grid[x - 1][y], num_grid[x + 1][y], num_grid[x][y - 1]]
            b = [(x - 1, y), (x, y - 1), (x + 1, y)]
        else:
            a = [num_grid[x + 1][y], num_grid[x - 1][y], num_grid[x][y + 1], num_grid[x][y - 1]]
            b = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
    return a, b


# For each individual number we want to create a set of the four numbers around it...
def ret_low_points(num_grid):
    """
    Create a list of points which all the numbers around it are lower than the current point
    :param num_grid: Rectangular grid of numbers in list form
    :return: List of points which all the numbers around it are lower than the current point
    """
    low_points = []
    for x in range(len(num_grid)):
        # Assume input is rectangular
        for y in range(len(num_grid[0])):
            a = get_adj_peaks(num_grid, x, y)[0]
            a = [int(x) for x in a]
            point = int(num_grid[x][y])
            if point < min(a):
                low_points.append(point)
    return low_points


assert sum([x + 1 for x in ret_low_points(d9e)]) == 15
a1 = sum([x + 1 for x in ret_low_points(d9)])


def find_next_unmarked_peak(x_len, y_len, basin_grid, next_basin):
    """
    Find the next peak that hasn't been marked and give it a basin mark
    :param x_len: X length of basin grid
    :param y_len: Y length of basin grid
    :param basin_grid: Co-ordinates of the basins
    :param next_basin: The next basin number to be assigned
    :return: Updated basin grid with new basin marked
    """
    for x in range(x_len):
        # Assume input is rectangular
        for y in range(y_len):
            if int(basin_grid[x][y]) == -1:
                # Update first number we get to
                basin_grid[x][y] = next_basin
                return basin_grid


def find_all_peaks_in_basin(x_len, y_len, basin_grid, curr_basin):
    """
    For a particular basin find all peaks in the same basin and mark them in basin grid
    :param x_len: X length of basin grid
    :param y_len: Y length of basin grid
    :param basin_grid: Co-ordinates of the basins
    :param curr_basin: The basin number to look for
    :return: Updated basin grid with new basins marked
    """
    # Count number of -1s at the beginning
    count = {0: [x for y in basin_grid for x in y].count(-1) + 1}
    i = 1
    count[i] = [x for y in basin_grid for x in y].count(-1)
    while count[i] < count[i - 1]:
        for x in range(x_len):
            # Assume input is rectangular
            for y in range(y_len):
                if int(basin_grid[x][y]) == curr_basin:
                    # Find surrounding co-ordinates
                    co_ords = get_adj_peaks(basin_grid, x, y)[1]
                    for c in co_ords:
                        if basin_grid[c[0]][c[1]] != -100:
                            basin_grid[c[0]][c[1]] = curr_basin
        i += 1
        count[i] = [x for y in basin_grid for x in y].count(-1)

    return basin_grid

def find_basins(num_grid):
    """
    Create a list of basins which have 9s or the edges surrounding it
    :param num_grid: Rectangular grid of numbers in list form
    :return: List of points which all the numbers around it are lower than the current point
    """
    # Befine our initial grid as -1s (to be marked)
    basin_grid = [[-1 for _ in range(len(num_grid[0]))] for _ in range(len(num_grid))]
    # First mark all our peaks (9s) as -100
    for x in range(len(num_grid)):
        # Assume input is rectangular
        for y in range(len(num_grid[0])):
            if int(num_grid[x][y]) == 9:
                basin_grid[x][y] = -100
            else:
                pass
    # Now slowly replace all -1s with a basin number
    # Use functions above to search for our next unmarked peak (-1) and then populate all other peaks around it that's in the same basin
    curr_basin = 0
    while ([x for y in basin_grid for x in y].count(-1) > 0) & (curr_basin < 10000):
        find_next_unmarked_peak(len(basin_grid), len(basin_grid[0]), basin_grid, curr_basin)
        find_all_peaks_in_basin(len(basin_grid), len(basin_grid[0]), basin_grid, curr_basin)
        curr_basin += 1

    # Finally find and keep the 3 biggest peaks
    counts = Counter([x for y in basin_grid for x in y if x != -100])
    big3 = counts.most_common(3)
    big3m = prod([x[1] for x in big3])

    return big3m


assert find_basins(d9e) == 1134
a2 = find_basins(d9)
