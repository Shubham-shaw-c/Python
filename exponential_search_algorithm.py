a = [2, 3, 4, 10, 40, 50, 60, 70, 80, 90]
x = 60
bound = 1
while bound < len(a) and a[bound] < x:
    bound *= 2
lo, hi = bound // 2, min(bound, len(a) - 1)
while lo <= hi:
    mid = (lo + hi) // 2
    if a[mid] == x:
        print("Found at", mid)
        break
    if a[mid] < x:
        lo = mid + 1
    else:
        hi = mid - 1
