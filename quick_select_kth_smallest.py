def quick_select(a, k):
    pivot = a[len(a) // 2]
    lows = [x for x in a if x < pivot]
    highs = [x for x in a if x > pivot]
    pivots = [x for x in a if x == pivot]
    if k < len(lows):
        return quick_select(lows, k)
    if k < len(lows) + len(pivots):
        return pivot
    return quick_select(highs, k - len(lows) - len(pivots))
print(quick_select([7, 10, 4, 3, 20, 15], 2))
