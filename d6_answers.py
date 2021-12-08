import numpy as np

# Import and split lines
d6 = open('Day 6 Data.txt', 'r').read().split(',')
d6 = [int(x) for x in d6]
d6e = [3, 4, 3, 1, 2]


def jelly_rep(jelly, days):
    """
    A function to return the total number of laternfish after an initial input of ages and the number of days

    :param jelly: The initial ages of all the lanternfish
    :param days: The number of days to iterate over
    :return: The total number of lanternfish
    """

    # Define ages which counts the number of fish with the days in the position of the array
    # Add the float 64 part to deal with overflow errors in part 2
    ages = [np.float64(0) for _ in range(9)]
    for f in jelly:
        # For each fish of age x add one to that position in the day
        ages[f] += 1

    for day in range(days):
        # As we go through the days shift everything to the left - this will move reproducing fish to 8
        # When ever that happens also add those fish to 6
        ages = np.roll(ages, -1)
        ages[6] += ages[8]

    return sum(ages)


assert jelly_rep(d6e, 80) == 5934
a1 = jelly_rep(d6, 80)

assert jelly_rep(d6e, 256) == 26984457539
a2 = jelly_rep(d6, 256)
