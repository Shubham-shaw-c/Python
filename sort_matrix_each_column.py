m = [[9, 3, 6], [1, 8, 2], [5, 4, 7]]
cols = [sorted(c) for c in zip(*m)]
print([list(r) for r in zip(*cols)])
