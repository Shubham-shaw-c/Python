import heapq
pq = []
heapq.heappush(pq, (2, "write report"))
heapq.heappush(pq, (1, "fix bug"))
heapq.heappush(pq, (3, "lunch"))
while pq:
    print(heapq.heappop(pq))
