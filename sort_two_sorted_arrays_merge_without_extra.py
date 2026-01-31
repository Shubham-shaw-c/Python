a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]
merged = sorted(a + b)
print(merged[:len(a)], merged[len(a):])
