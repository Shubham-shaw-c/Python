data = [9, 4, 7, 2, 6]
for p in range(len(data) - 1):
    for j in range(len(data) - 1 - p):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
    print("Pass", p + 1, data)
