data = [64, 34, 25, 12, 22, 11, 90]
n = len(data)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
print(data)
