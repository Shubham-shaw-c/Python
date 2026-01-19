import heapq
data = [5, 9, 1, 7, 3, 8]
heapq.heapify(data)
print([heapq.heappop(data) for _ in range(len(data))])
