data = [7, 10, 4, 3, 20, 15]
k = 3
for i in range(k):
    m = min(range(i, len(data)), key=lambda x: data[x])
    data[i], data[m] = data[m], data[i]
print(data[:k])
