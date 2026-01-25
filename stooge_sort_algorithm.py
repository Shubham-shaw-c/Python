def stooge(a, l, h):
    if a[l] > a[h]:
        a[l], a[h] = a[h], a[l]
    if h - l + 1 > 2:
        t = (h - l + 1) // 3
        stooge(a, l, h - t)
        stooge(a, l + t, h)
        stooge(a, l, h - t)
data = [2, 4, 5, 3, 1]
stooge(data, 0, len(data) - 1)
print(data)
