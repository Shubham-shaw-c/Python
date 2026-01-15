data = [(4, "a"), (2, "b"), (4, "c"), (1, "d")]
for i in range(len(data)):
    m = i
    for j in range(i + 1, len(data)):
        if data[j][0] < data[m][0]:
            m = j
    item = data.pop(m)
    data.insert(i, item)
print(data)
