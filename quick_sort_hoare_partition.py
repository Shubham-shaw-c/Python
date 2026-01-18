def quick_sort(a, lo, hi):
    if lo >= hi:
        return
    pivot = a[(lo + hi) // 2]
    i, j = lo - 1, hi + 1
    while True:
        i += 1
        while a[i] < pivot:
            i += 1
        j -= 1
        while a[j] > pivot:
            j -= 1
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
    quick_sort(a, lo, j)
    quick_sort(a, j + 1, hi)
data = [9, 3, 7, 1, 8, 2, 6]
quick_sort(data, 0, len(data) - 1)
print(data)
