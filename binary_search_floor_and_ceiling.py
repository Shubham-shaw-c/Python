a = [1, 2, 8, 10, 10, 12, 19]
x = 9
floor = max((v for v in a if v <= x), default=None)
ceil = min((v for v in a if v >= x), default=None)
print(floor, ceil)
