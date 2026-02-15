from collections import deque
q = deque(["1"])
for _ in range(8):
    s = q.popleft()
    print(s, end=" ")
    q.append(s + "0")
    q.append(s + "1")
print()
