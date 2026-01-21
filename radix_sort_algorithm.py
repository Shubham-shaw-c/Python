data = [170, 45, 75, 90, 802, 24, 2, 66]
exp = 1
while max(data) // exp > 0:
    buckets = [[] for _ in range(10)]
    for x in data:
        buckets[(x // exp) % 10].append(x)
    data = [x for b in buckets for x in b]
    exp *= 10
print(data)
