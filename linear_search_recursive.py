def search(data, key, i=0):
    if i == len(data):
        return -1
    if data[i] == key:
        return i
    return search(data, key, i + 1)
print(search([5, 8, 2, 9], 2))
