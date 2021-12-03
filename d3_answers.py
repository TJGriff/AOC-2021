# Import and split lines
d3 = open('Day 3 Data.txt', 'r').read().split('\n')

# The binary number is stored as a string but that doesn't matter for out purposes

# We want to loop through the length
def mode(lst):
    """ Function that returns most common item in a list"""

    return max(set(lst), key=lst.count)


a2gam = [mode([x[y] for x in d3]) for y in range(len(d3[0]))]

# Now need to convert each to number and do 1- to get eps
a2gam = [int(x) for x in a2gam]

a2ep = [x + 1 if x == 0 else x - 1 for x in a2gam]

# Convert from list to number (via a string again...)
a2gamnm = ''.join([str(x) for x in a2gam])
a2epnm = ''.join([str(x) for x in a2ep])

# Convert to decimal
gamma = int(a2gamnm, 2)
epsilon = int(a2epnm, 2)

a3a = gamma * epsilon

# PART 2

# Now need to loop through one by one and delete as we go
# When we keep the maxes the 0 will be kept in the case of ties - we want 1s so add an extra 1 to our list
# in the way the challenge wants us to

# For O2 we want 1s to win so we're good
# Create a copy as we filter values out
d3o2 = d3.copy()
# For each bit in the numbers...
c = len(d3[0])

for y in range(c):
    # Create a list with the yth bit
    lst = [x[y] for x in d3o2]
    # Give our list an extra one to swing ties in favour of 1s
    lst.insert(0, '1')
    # Find the mode
    a = mode(lst)
    d3o2 = [x for x in d3o2 if x[y] == a]
    print(len(d3o2), y)

# Now for c02 the opposite giving 0s a headstart
d3co2 = d3.copy()

for y in range(c):
    # Create a list with the yth bit
    lst = [x[y] for x in d3o2]
    # Find the min (can't be bothered to write out the function again!)
    a = min(set(lst), key=lst.count)
    d3co2 = [x for x in d3co2 if x[y] == a]

# Convert from list to number (via a string again...)
a2co2 = ''.join([str(x) for x in d3co2])
a2o2 = ''.join([str(x) for x in d3o2])

# Convert to decimal
co2 = int(a2co2, 2)
o2 = int(a2o2, 2)

a3b = co2 * o2
