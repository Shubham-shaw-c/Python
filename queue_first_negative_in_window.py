from collections import deque
a = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
neg = deque()
out = []
for i, x in enumerate(a):
    if x < 0:
        neg.append(i)
    if i >= k - 1:
        while neg and neg[0] <= i - k:
            neg.popleft()
        out.append(a[neg[0]] if neg else 0)
print(out)
