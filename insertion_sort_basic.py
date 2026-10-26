data = [12, 11, 13, 5, 6]
for i in range(1, len(data)):
    key = data[i]
    j = i - 1
    while j >= 0 and data[j] > key:
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = key
print(data)
