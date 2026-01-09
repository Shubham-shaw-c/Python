a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
x = 70
lo, hi = 0, len(a) - 1
while lo <= hi and a[lo] <= x <= a[hi]:
    pos = lo + (x - a[lo]) * (hi - lo) // (a[hi] - a[lo])
    if a[pos] == x:
        print("Found at", pos)
        break
    if a[pos] < x:
        lo = pos + 1
    else:
        hi = pos - 1
