def is_sorted(a):
    return all(a[i] <= a[i + 1] for i in range(len(a) - 1))
print(is_sorted([1, 2, 2, 5]), is_sorted([3, 1, 2]))
