a = [15, 18, 2, 3, 6, 12]
target = 3
lo, hi = 0, len(a) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if a[mid] == target:
        print(mid)
        break
    if a[lo] <= a[mid]:
        if a[lo] <= target < a[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    else:
        if a[mid] < target <= a[hi]:
            lo = mid + 1
        else:
            hi = mid - 1
