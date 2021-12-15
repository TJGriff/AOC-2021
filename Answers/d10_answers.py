from statistics import median

d10 = open("Data/Day 10 Data.txt", 'r').read().split("\n")
d10e = [
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '{([(<{}[<>[]}>{[]{[(<()>',
    '(((({<>}<{<{<>}{[]{[]{}',
    '[[<[([]))<([[{}[[()]]]',
    '[{[{({}]{}}([{[{{{}}([]',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '[<(<(<(<{}))><([]([]()',
    '<{([([[(<>()){}]>(<<{{',
    '<{([{{}}[<[[[<>{}]]]>[]]',
]

# As we go through the string there are 3 options
#   a. "Open" string: Add character and continue
#   b. "Closed" string same as the last: Delete the last character and don't add the closed string
#   c. "Closed" string not the same as the last: Stop going through the string and record the character

# First define our opening and closing pairs
bracket_pairs = {'{': '}', '(': ')', '<': '>', '[': ']'}
open_lst = list(bracket_pairs.keys())
bracket_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}


def find_first_illegal_char(nav_sys_strs):
    """
    Go through the strings and find the corrupted characters
    :param nav_sys_strs: List of string of brackets
    :return: List of corrupted characters
    """
    corrupted_chars = []
    open_lines = {}

    for idx, line in enumerate(nav_sys_strs):
        brack_canc_tracker = []
        c = 0
        for i in range(len(line)):
            # This loops through until first corruption cancelling off pairs of brackets
            # If open add to our list
            if line[i] in open_lst:
                brack_canc_tracker.append(line[i])
            # If first item is closed then add to our corrupted_chars and break
            elif i == 0:
                corrupted_chars.append(line[i])
                c = 1
                break
            else:
                if bracket_pairs[brack_canc_tracker[-1]] == line[i]:
                    brack_canc_tracker = brack_canc_tracker[:-1]
                else:
                    corrupted_chars.append(line[i])
                    c = 1
                    break
        if c == 0:
            open_lines[idx] = brack_canc_tracker
    return corrupted_chars, open_lines


t = find_first_illegal_char(d10e)[0]
assert sum([bracket_scores[c] for c in t]) == 26397
a1p = find_first_illegal_char(d10)[0]
a1 = sum([bracket_scores[c] for c in a1p])

# Now we need to use a similar logic to before but remove corrupted and go all the way to the end of the string
# Adapt function above to create our open lines

new_scores = {')': 1, ']': 2, '}': 3, '>': 4}


# Now for our open lines we want to reverse these, map the them to the closed bracket then count the score
def rev_map_count(lst):
    score = []
    for b in lst:
        item_score = 0
        rev_open = [b[x] for x in range(len(b) - 1, -1, -1)]
        rev_closed = [bracket_pairs[y] for y in rev_open]
        for i in rev_closed:
            item_score = item_score * 5 + new_scores[i]
        score.append(item_score)
    return score


d10e_p2 = list(find_first_illegal_char(d10e)[1].values())
d10_p2 = list(find_first_illegal_char(d10)[1].values())

assert median(rev_map_count(d10e_p2)) == 288957
a2 = median(rev_map_count(d10_p2))
