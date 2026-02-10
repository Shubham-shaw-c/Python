from collections import deque
class Queue:
    def __init__(self):
        self.q = deque()
    def enqueue(self, x):
        self.q.append(x)
    def dequeue(self):
        return self.q.popleft()
    def size(self):
        return len(self.q)
q = Queue()
for x in "ABC":
    q.enqueue(x)
print(q.dequeue(), q.size())
