a = [1, 2, 2, 2, 3, 4, 4, 5]
target = 2
lo, hi = 0, len(a) - 1
ans = -1
while lo <= hi:
    mid = (lo + hi) // 2
    if a[mid] == target:
        ans = mid
        hi = mid - 1
    elif a[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
print(ans)
