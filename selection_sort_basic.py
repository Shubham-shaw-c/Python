data = [29, 10, 14, 37, 13]
for i in range(len(data)):
    m = i
    for j in range(i + 1, len(data)):
        if data[j] < data[m]:
            m = j
    data[i], data[m] = data[m], data[i]
print(data)
