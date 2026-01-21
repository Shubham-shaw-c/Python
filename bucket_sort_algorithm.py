data = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
buckets = [[] for _ in range(10)]
for x in data:
    buckets[int(x * 10)].append(x)
result = []
for b in buckets:
    result += sorted(b)
print(result)
