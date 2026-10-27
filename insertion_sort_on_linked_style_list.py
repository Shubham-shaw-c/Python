data = [3, 1, 2]
out = []
for x in data:
    pos = 0
    while pos < len(out) and out[pos] < x:
        pos += 1
    out.insert(pos, x)
print(out)
