data = [12, 3, 5, 7, 19, 26, 8]
s = sorted(data)
n = len(s)
print((s[n // 2] + s[~(n // 2)]) / 2)
