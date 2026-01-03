def bsearch(a, t, lo, hi):
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if a[mid] == t:
        return mid
    if a[mid] < t:
        return bsearch(a, t, mid + 1, hi)
    return bsearch(a, t, lo, mid - 1)
arr = [1, 3, 5, 7, 9, 11, 13]
print(bsearch(arr, 11, 0, len(arr) - 1))
