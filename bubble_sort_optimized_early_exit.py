data = [5, 1, 4, 2, 8]
n = len(data)
for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
            swapped = True
    if not swapped:
        break
print(data)
