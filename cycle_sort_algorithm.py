data = [20, 40, 50, 10, 30]
for start in range(len(data) - 1):
    item = data[start]
    pos = start + sum(1 for x in data[start + 1:] if x < item)
    if pos == start:
        continue
    while item == data[pos]:
        pos += 1
    data[pos], item = item, data[pos]
    while pos != start:
        pos = start + sum(1 for x in data[start + 1:] if x < item)
        while item == data[pos]:
            pos += 1
        data[pos], item = item, data[pos]
print(data)
