a = [1, 4, 9, 14, 21, 30, 42, 55]
x = 30
lo, hi = 0, len(a) - 1
while lo <= hi:
    third = (hi - lo) // 3
    m1, m2 = lo + third, hi - third
    if a[m1] == x:
        print(m1)
        break
    if a[m2] == x:
        print(m2)
        break
    if x < a[m1]:
        hi = m1 - 1
    elif x > a[m2]:
        lo = m2 + 1
    else:
        lo, hi = m1 + 1, m2 - 1
