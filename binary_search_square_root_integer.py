n = 150
lo, hi = 0, n
while lo <= hi:
    mid = (lo + hi) // 2
    if mid * mid <= n:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1
print(ans)
