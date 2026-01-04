from bisect import bisect_left, bisect_right
a = [1, 2, 2, 2, 3, 4, 4, 5]
print(bisect_right(a, 2) - bisect_left(a, 2))
