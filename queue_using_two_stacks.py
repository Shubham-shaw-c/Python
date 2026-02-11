class TwoStackQueue:
    def __init__(self):
        self.inbox, self.outbox = [], []
    def push(self, x):
        self.inbox.append(x)
    def pop(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()
q = TwoStackQueue()
for i in range(1, 4):
    q.push(i)
print(q.pop(), q.pop())
q.push(4)
print(q.pop(), q.pop())
