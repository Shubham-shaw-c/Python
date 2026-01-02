data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
low, high = 0, len(data) - 1
while low <= high:
    mid = (low + high) // 2
    if data[mid] == target:
        print("Found at", mid)
        break
    if data[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not found")
