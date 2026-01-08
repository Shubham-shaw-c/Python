m = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16], [10, 13, 14, 17]]
target = 9
r, c = 0, len(m[0]) - 1
while r < len(m) and c >= 0:
    if m[r][c] == target:
        print("Found", r, c)
        break
    if m[r][c] > target:
        c -= 1
    else:
        r += 1
