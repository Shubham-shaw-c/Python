def heapify(a, n, i):
    largest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)
data = [12, 11, 13, 5, 6, 7]
n = len(data)
for i in range(n // 2 - 1, -1, -1):
    heapify(data, n, i)
for i in range(n - 1, 0, -1):
    data[0], data[i] = data[i], data[0]
    heapify(data, i, 0)
print(data)
