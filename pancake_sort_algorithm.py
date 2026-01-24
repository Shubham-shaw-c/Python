def flip(a, k):
    a[:k + 1] = a[:k + 1][::-1]
data = [3, 6, 1, 9, 4]
for size in range(len(data), 1, -1):
    m = data.index(max(data[:size]))
    if m != size - 1:
        flip(data, m)
        flip(data, size - 1)
print(data)
