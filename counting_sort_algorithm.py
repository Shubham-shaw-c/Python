data = [4, 2, 2, 8, 3, 3, 1]
count = [0] * (max(data) + 1)
for x in data:
    count[x] += 1
out = []
for v, c in enumerate(count):
    out += [v] * c
print(out)
