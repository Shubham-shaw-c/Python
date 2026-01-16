def count(a):
    if len(a) <= 1:
        return a, 0
    mid = len(a) // 2
    l, x = count(a[:mid])
    r, y = count(a[mid:])
    out, inv = [], x + y
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            out.append(l[i])
            i += 1
        else:
            out.append(r[j])
            inv += len(l) - i
            j += 1
    return out + l[i:] + r[j:], inv
print(count([8, 4, 2, 1])[1])
