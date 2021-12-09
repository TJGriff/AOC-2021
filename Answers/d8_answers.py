from collections import Counter

# Import and split lines
d81 = open("Data/Day 8 Data.txt", 'r').read().split('\n')
d8e1 = open("Data/Day 8 Example.txt", 'r').read().split('\n')
d8 = [[y.strip().split(' ') for y in x.split('|') if y != ''] for x in d81]
d8e = [[y.strip().split(' ') for y in x.split('|') if y != ''] for x in d8e1]


# First part is easy just count the number of 2, 3, 4 and 7 character strings
def count_len_str(lst, lens):
    """
    Return the number of times a specific length of string occurs
    :param lst: A list of strings to count the specific lengths of
    :param lens: The specific lengths we're interested in
    :return: Number of times that length appears
    """

    cnt = 0
    for a in lst:
        if len(a) in lens:
            cnt += 1

    return cnt


assert count_len_str([a for b in d8e for a in b[1]], [2, 3, 4, 7]) == 26
a1 = count_len_str([a for b in d8 for a in b[1]], [2, 3, 4, 7])

# To derive the full number we need to iteratively work out individual segments
# numbers 1, 7, 4  and 8 of length 2, 3, 4 and 7 are already known
# 7 slots

# First we need to write out the definition of the numbers in 77d
ss = [[1, 1, 1, 0, 1, 1, 1],
      [0, 0, 1, 0, 0, 1, 0],
      [1, 0, 1, 1, 1, 0, 1],
      [1, 0, 1, 1, 0, 1, 1],
      [0, 1, 1, 1, 0, 1, 0],
      [1, 1, 0, 1, 0, 1, 1],
      [1, 1, 0, 1, 1, 1, 1],
      [1, 0, 1, 0, 0, 1, 0],
      [1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 0, 1, 1],
      ]

# Now we distinguish the numbers by counting the number of times each letter occurs
# Then work out is corresponding position in our ss grid above
# e.g. the (a) string (col 0) along the top of the 77d display appears 8 times across the 10 numbers,
# a trait only shared by the (c) string (col (2))
# We can sum these traits for each individual number to work out a unique identifier for the number

dict77d = {a: sum([item[a] for item in ss]) for a in range(7)}
map = {a: sum([dict77d[i] for i, num in enumerate(s) if num == 1]) for a, s in enumerate(ss)}

# So for an unknown dataset we want to apply the revers
inv_map = {v: k for k, v in map.items()}


# Now for each letter in our input sum the number of times each occur
def find_num_map(input, output):
    """
    For an input/output display work out the number and sum the output
    :param input: 10 numbers displayed in letters 77d format
    :param output: 4 numbers displayed in letters 77d format
    :return: sum of the numbers in the output
    """

    counts = Counter([b for a in input for b in a])
    total = [sum([counts[d] for d in a]) for a in input]
    nums = [inv_map[a] for a in total]
    num_dict = {"".join(sorted(k)): v for k, v in zip(input, nums)}
    num_output = [num_dict["".join(sorted(o))] for o in output]
    return int("".join([str(n) for n in num_output]))


assert sum([find_num_map(d77[0], d77[1]) for d77 in d8e]) == 61229
a2 = sum([find_num_map(d77[0], d77[1]) for d77 in d8])

