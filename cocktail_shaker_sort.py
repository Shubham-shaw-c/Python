data = [5, 1, 4, 2, 8, 0, 2]
lo, hi = 0, len(data) - 1
swapped = True
while swapped:
    swapped = False
    for i in range(lo, hi):
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
            swapped = True
    hi -= 1
    for i in range(hi, lo, -1):
        if data[i] < data[i - 1]:
            data[i], data[i - 1] = data[i - 1], data[i]
            swapped = True
    lo += 1
print(data)
