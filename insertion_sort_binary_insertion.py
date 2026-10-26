from bisect import insort
data = [37, 23, 0, 17, 12, 72, 31]
result = []
for x in data:
    insort(result, x)
print(result)
