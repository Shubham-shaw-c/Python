data = [23, 12, 1, 8, 34, 54, 2, 3]
gap = len(data) // 2
while gap > 0:
    for i in range(gap, len(data)):
        temp = data[i]
        j = i
        while j >= gap and data[j - gap] > temp:
            data[j] = data[j - gap]
            j -= gap
        data[j] = temp
    gap //= 2
print(data)
