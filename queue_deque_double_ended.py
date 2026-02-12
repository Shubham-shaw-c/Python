from collections import deque
d = deque([2, 3, 4])
d.appendleft(1)
d.append(5)
d.rotate(2)
print(d, d.pop(), d.popleft())
