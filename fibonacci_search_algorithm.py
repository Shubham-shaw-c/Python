a = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
x = 85
f2, f1 = 0, 1
f = f2 + f1
while f < len(a):
    f2, f1 = f1, f
    f = f2 + f1
offset = -1
while f > 1:
    i = min(offset + f2, len(a) - 1)
    if a[i] < x:
        f, f1, f2 = f1, f2, f1 - f2
        offset = i
    elif a[i] > x:
        f, f1, f2 = f2, f1 - f2, f2 - (f1 - f2)
    else:
        print("Found at", i)
        break
