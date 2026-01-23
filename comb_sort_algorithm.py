data = [8, 4, 1, 56, 3, -44, 23, -6, 28, 0]
gap = len(data)
swapped = True
while gap > 1 or swapped:
    gap = max(1, int(gap / 1.3))
    swapped = False
    for i in range(len(data) - gap):
        if data[i] > data[i + gap]:
            data[i], data[i + gap] = data[i + gap], data[i]
            swapped = True
print(data)
