data = [34, 2, 10, -9, 15, 7]
done = False
while not done:
    done = True
    for start in (1, 0):
        for i in range(start, len(data) - 1, 2):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                done = False
print(data)
