digits = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab"
counts = Counter(digits)
known = {"acedgfb": 8, "cdfbe": 5, "gcdfa": 2, "fbcad": 3, "dab": 7,
         "cefabd": 9, "cdfgeb": 6, "eafb": 4, "cagedb": 0, "ab": 1}
compute = lambda s: sum(counts[c] for c in s)
key = {compute(digit):known[digit] for digit in digits.split()}