import math
a = [0, 1, 3, 5, 8, 13, 21, 34, 55, 89]
target = 34
step = int(math.sqrt(len(a)))
prev = 0
while prev < len(a) and a[min(step, len(a)) - 1] < target:
    prev = step
    step += int(math.sqrt(len(a)))
for i in range(prev, min(step, len(a))):
    if a[i] == target:
        print("Found at", i)
