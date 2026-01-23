data = [34, 2, 10, -9, 15]
i = 0
while i < len(data):
    if i == 0 or data[i] >= data[i - 1]:
        i += 1
    else:
        data[i], data[i - 1] = data[i - 1], data[i]
        i -= 1
print(data)
