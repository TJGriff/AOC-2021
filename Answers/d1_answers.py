# Import and split lines
d1 = open('../Data/Day 1 Data', 'r').read().split()
# Convert strings in list to numbers
d1 = [int(x) for x in d1]


def d1_count_increasing(lst):
    """This function counts the number of increasing steps in a list
    :arg lst: A list containing integer values

    :return An integer containing the number of increasing steps in the list

    """

    # Create a new list with the first item twice the same and then remove the last item and subtract the lists from
    # each other

    # Copy the first item
    lsta = lst.copy()
    # Insert the first item of the list again at the beginning of the list
    lsta.insert(0, d1[0])
    # Remove the last item from the list
    lstb = lsta[:-1]
    # Now subtract the 2 by using list comprehension and keep only the values > 0
    lstc = [a - b for a, b in zip(lst, lstb) if a - b > 0]
    # Now see how many values there are and that's our answer
    return len(lstc)

# Calculate the answer to 1a
d1aanswr = d1_count_increasing(d1)

# Now need to create a new list which includes the sum of the first 3 second 3 etc.
d1b = [sum(d1[y:y+3]) for y in range(len(d1)-3)]

# Now put it through our function above
d1banswr = d1_count_increasing(d1b)
