def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    return quick_sort([x for x in a if x < pivot]) + [x for x in a if x == pivot] + quick_sort([x for x in a if x > pivot])
print(quick_sort([10, 7, 8, 9, 1, 5, 3, 3]))
