def merge_sort(a, lo, hi):
    if hi - lo < 2:
        return
    mid = (lo + hi) // 2
    merge_sort(a, lo, mid)
    merge_sort(a, mid, hi)
    merged = []
    i, j = lo, mid
    while i < mid and j < hi:
        if a[i] <= a[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(a[j])
            j += 1
    merged += a[i:mid] + a[j:hi]
    a[lo:hi] = merged
data = [5, 2, 9, 1, 5, 6, 0]
merge_sort(data, 0, len(data))
print(data)
