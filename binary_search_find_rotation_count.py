a = [15, 18, 2, 3, 6, 12]
lo, hi = 0, len(a) - 1
while lo < hi:
    mid = (lo + hi) // 2
    if a[mid] > a[hi]:
        lo = mid + 1
    else:
        hi = mid
print("Rotated by", lo)
