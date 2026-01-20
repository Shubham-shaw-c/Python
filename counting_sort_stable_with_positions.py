data = [4, 2, 2, 8, 3, 3, 1]
k = max(data) + 1
count = [0] * k
for x in data:
    count[x] += 1
for i in range(1, k):
    count[i] += count[i - 1]
out = [0] * len(data)
for x in reversed(data):
    count[x] -= 1
    out[count[x]] = x
print(out)
