data = [8, 3, 6, 1, 9]
target = 1
data.append(target)
i = 0
while data[i] != target:
    i += 1
data.pop()
print("Found at", i if i < len(data) else "not found")
