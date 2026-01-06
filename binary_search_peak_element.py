a = [1, 3, 8, 12, 9, 4, 2]
lo, hi = 0, len(a) - 1
while lo < hi:
    mid = (lo + hi) // 2
    if a[mid] < a[mid + 1]:
        lo = mid + 1
    else:
        hi = mid
print(a[lo], lo)
