# This code actually looks half decent
from collections import Counter

# Import and split lines
d5d1 = open('../Data/Day 5 Data.txt', 'r').read().split('\n')
d5d1e = open('../Data/Day 5 Data Example.txt', 'r').read().split('\n')
# Use arrow as delimiter, strip spaces, split co-ordinates and convert to int
d5d = [[[int(y) for y in x.strip().split(',')] for x in map.split('->')] for map in d5d1]
d5de = [[[int(y) for y in x.strip().split(',')] for x in map.split('->')] for map in d5d1e]


class coordinate_map(object):
    # Input of the format [[x1,y1], [x2,y2]]
    def __init__(self, xy1xy2):
        self.x1 = xy1xy2[0][0]
        self.y1 = xy1xy2[0][1]
        self.x2 = xy1xy2[1][0]
        self.y2 = xy1xy2[1][1]

    def getxy1(self):
        return [self.x1, self.x2]

    def getxy2(self):
        return [self.x2, self.y2]

    def __repr__(self):
        return str(self.getxy1()) + ' -> ' + str(self.getxy2())

    def xmatch(self):
        return self.x1 == self.x2

    def ymatch(self):
        return self.y1 == self.y2

    def maxx(self):
        return max(self.x1, self.x2)

    def maxy(self):
        return max(self.y1, self.y2)

    def minx(self):
        return min(self.x1, self.x2)

    def miny(self):
        return min(self.y1, self.y2)

    def updiag(self):
        return (self.x2 - self.x1) == (self.y2 - self.y1)

    def downdiag(self):
        return (self.x2 - self.x1) == -(self.y2 - self.y1)

    def between_coordinates(self):
        if self.xmatch():
            return [[self.x1, newy] for newy in range(self.miny(), self.maxy() + 1)]
        elif self.ymatch():
            return [[newx, self.y1] for newx in range(self.minx(), self.maxx() + 1)]
        # If match then return empty for part one
        else:
            return []

    def between_coordinates_diag(self):
        if self.xmatch():
            return [[self.x1, newy] for newy in range(self.miny(), self.maxy() + 1)]
        elif self.ymatch():
            return [[newx, self.y1] for newx in range(self.minx(), self.maxx() + 1)]
        elif self.updiag():
            return [[self.minx() + step, self.miny() + step] for step in range(self.maxx() - self.minx() + 1)]
        elif self.downdiag():
            return [[self.minx() + step, self.maxy() - step] for step in range(self.maxx() - self.minx() + 1)]
        # If match then return empty for part one
        else:
            return []

# Load all the input co-ordinates into our class
co_main = [coordinate_map(x) for x in d5d]
co_eg = [coordinate_map(x) for x in d5de]


def find_hotpoints(co_pairs):
    # Calculate all the co-ordinates in a grid
    between_co = [x.between_coordinates() for x in co_pairs]
    # Unnest the list and turn into tuples to enables counting
    between_co_comb = [tuple(x) for y in between_co for x in y]
    occurrences = Counter(between_co_comb)
    return [key for key, value in occurrences.items() if value > 1]


assert len(find_hotpoints(co_eg)) == 5
a1 = len(find_hotpoints(co_main))

def find_hotpoints_diag(co_pairs):
    # Calculate all the co-ordinates in a grid
    between_co = [x.between_coordinates_diag() for x in co_pairs]
    # Unnest the list and turn into tuples to enables counting
    between_co_comb = [tuple(x) for y in between_co for x in y]
    occurrences = Counter(between_co_comb)
    return [key for key, value in occurrences.items() if value > 1]


assert len(find_hotpoints_diag(co_eg)) == 12
a2 = len(find_hotpoints_diag(co_main))
