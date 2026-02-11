from collections import deque
class QStack:
    def __init__(self):
        self.q = deque()
    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    def pop(self):
        return self.q.popleft()
s = QStack()
for i in (1, 2, 3):
    s.push(i)
print(s.pop(), s.pop(), s.pop())
