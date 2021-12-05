# THis code could be better
# Import and split lines
d4d = open('Day 4 Draw.txt', 'r').read().split(',')
# Import and split lines in eg
d4de = open('Day 4 Draw EG.txt', 'r').read().split(',')
# convert to ints
d4d = [int(x) for x in d4d]
d4de = [int(x) for x in d4de]
d4gp = open('Day 4 Grids.txt', 'r').read().split('\n\n')
d4gpe = open('Day 4 Grid Eg.txt', 'r').read().split('\n\n')
# split out the lines in each grid
d4gp2 = [x.split('\n') for x in d4gp]
d4gpe2 = [x.split('\n') for x in d4gpe]
# now convert into ints
# x = list of grads, y = list of rows, z = individual number, some records had 2 spaces or random spaces so remove
# those when we split
d4g = [[[int(z) for z in y.split(' ') if z != ''] for y in x] for x in d4gp2]
d4ge = [[[int(z) for z in y.split(' ') if z != ''] for y in x] for x in d4gpe2]


# We now have our grids nicely recorded but need to work out how to work out the objective
# If the sum of one of the columns equal 5 then we win or if the sum of one of the rows is 5 then we've won
# Finally for the diagonal we need to check if [1,1], [2,2] ..., [5,5] is marked or [1,5], [2,4] ... [4,2], [5,2]
# is marked

# I'm going to approach this by created a check win function with all the individual checks

def row_win(grid):
    """ Function to work out if a 5x5 grid of binary mark values is a success due to rows
     (five lists have a row that wins)"""
    # row is our lists, do sum each list and take the max to see if any sum to 5
    if max([sum(grid[row]) for row in range(5)]) == 5:
        return 1
    else:
        return 0


def column_win(grid):
    """ Function to work out if a 5x5 grid of binary mark values is a success due to columns
     (five lists have a column that wins)"""
    # row is just the first item in the list so easy
    if max([sum([row[column] for row in grid]) for column in range(5)]) == 5:
        return 1
    else:
        return 0


def diagonal_tl_to_br_win(grid):
    """ Function to work out if a 5x5 grid of binary mark values is a success due to diagonal from
    top left to bottom right"""
    # row is just the first item in the list so easy
    if sum([grid[row_column][row_column] for row_column in range(5)]) == 5:
        return 1
    else:
        return 0


def diagonal_bl_to_tr_win(grid):
    """ Function to work out if a 5x5 grid of binary mark values is a success due to diagonal from
    top left to bottom right"""
    # row is just the first item in the list so easy
    if sum([grid[4 - row_column][row_column] for row_column in range(5)]) == 5:
        return 1
    else:
        return 0


# Now combine all these together into one check
# Apparently diagonals don't count...
def win_chk(grid):
    return max(column_win(grid), row_win(grid))


# Now have the code ready to check if there's a win need to create a process to mark our grids
# The win checks involve starting everything as unmarked (0s) and then changing them to 1 after each number
# is uncovered
# When one number goes through we work out the winning grid
# Now we need some more functions to check each grid for the number and then return the location
def find_num(grid, num):
    """THis function looks for a number in a grid and returns the co-ordinates of returns (-1,-1)"""
    for row in range(5):
        for column in range(5):
            if grid[row][column] == num:
                return [row, column]
            elif (row == 4) & (column == 4):
                return [-1, -1]
            else:
                pass
    raise Exception("Something has gone wrong here!")


# Have to define in the long way as apparently defining it with multiplications changes all items at once......
init_mark_grids = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(100)]


# Now create a function to update the mark grids if the number is in each grid
def number_update(grids, num, mark_grids):
    for loop_num, grid in enumerate(grids):
        # If our number is marked...
        # print(loop_num)
        # print(grid)
        # print(find_num(grid, num))
        if find_num(grid, num) != [-1, -1]:
            # Get the position of where it is
            row_col = find_num(grid, num)
            # Change the value in our grids to 1
            mark_grids[loop_num][row_col[0]][row_col[1]] = 1

        else:
            pass

    # Return the updated marked grids
    return mark_grids


# Now let's follow the process to check which grid wins
def play_game(numbers, grids, mark_grids):
    for draw in numbers:
        # Update our mark grid with the latest number
        mark_grids = number_update(grids, draw, mark_grids)
        print(mark_grids)
        # Check to see if a grid was won
        winning_grids = [grid_num for grid_num, grid in enumerate(mark_grids) if win_chk(grid) == 1]
        if len(winning_grids) != 0:
            if len(winning_grids) > 1:
                return """Multiple won together!"""
            else:
                winning_grid = winning_grids[0]
            # Create a list to store unmarked numbers from the wiining grid
            num_list = []
            for column in range(5):
                for row in range(5):
                    # Check value in init_mark_grids
                    if init_mark_grids[winning_grid][row][column] == 0:
                        num_list.append(d4g[winning_grid][row][column])

            return winning_grid, sum(num_list) * draw

    # Hopefully we'll find a winner so this isn't necessary!
    return []


# let's play!
winner, score = play_game(d4d, d4g, init_mark_grids)


# Part two - for this we want to change the play game function to win last

# This if very similar to play game except now instead of returning the instant we find something we keep on
# going until we've found everything and only then stop
init_mark_grids = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(100)]


def win_last(numbers, grids, mark_grids):
    for draw in numbers:
        # Update our mark grid with the latest number
        mark_grids = number_update(grids, draw, mark_grids)
        print(mark_grids)
        # Check to see if a grid was won
        winning_grids = [grid_num for grid_num, grid in enumerate(mark_grids) if win_chk(grid) == 1]
        if len(winning_grids) == 99:
            # Find the last grid
            last_grid = [x for x in range(100) if x not in winning_grids][0]
        elif len(winning_grids) == 100:
            num_list = []
            for column in range(5):
                for row in range(5):
                    # Check value in init_mark_grids
                    if init_mark_grids[last_grid][row][column] == 0:
                        num_list.append(d4g[last_grid][row][column])
            return last_grid, sum(num_list) * draw

    # Hopefully we'll find a winner so this isn't necessary!
    return []


last_grid, score = win_last(d4d, d4g, init_mark_grids)

