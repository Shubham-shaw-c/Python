from bisect import bisect_left
a = [1, 3, 5, 6, 10]
for t in (5, 2, 7, 0, 11):
    print(t, bisect_left(a, t))
