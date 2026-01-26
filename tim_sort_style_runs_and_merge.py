import heapq
data = [5, 21, 7, 23, 19, 3, 1, 8]
runs = [sorted(data[i:i + 4]) for i in range(0, len(data), 4)]
print(list(heapq.merge(*runs)))
