# Import and split lines
d2 = open('../Data/Day 2 Data.txt', 'r').read().split('\n')

movements = [x.split()[0] for x in d2]
size = [int(x.split()[1]) for x in d2]

# Let x represent the position and y represent the depth
# Starting positions
x = 0
y = 0


for i in range(len(size)):
    if movements[i] == 'forward':
        x += size[i]
    elif movements[i] == 'down':
        y += size[i]
    elif movements[i] == 'up':
        y -= size[i]
    else:
        raise ValueError('Movement not recognised')

a1 = x*y

### PART 2

# Let x represent the position and y represent the depth
# Starting positions
x = 0
y = 0
z = 0


for i in range(len(size)):
    if movements[i] == 'forward':
        x += size[i]
        y += (z * size[i])
    elif movements[i] == 'down':
        z += size[i]
    elif movements[i] == 'up':
        z -= size[i]
    else:
        raise ValueError('Movement not recognised')
    print(x,y,z)





