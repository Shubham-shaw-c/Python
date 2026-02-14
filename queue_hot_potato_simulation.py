from collections import deque
q = deque(["Ann", "Ben", "Cat", "Dan", "Eve"])
passes = 7
while len(q) > 1:
    q.rotate(-passes)
    print(q.pop(), "is out")
print(q[0], "wins")
