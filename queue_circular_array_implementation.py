class CircularQueue:
    def __init__(self, cap):
        self.a = [None] * cap
        self.cap = cap
        self.head = self.count = 0
    def enqueue(self, x):
        if self.count == self.cap:
            return False
        self.a[(self.head + self.count) % self.cap] = x
        self.count += 1
        return True
    def dequeue(self):
        x = self.a[self.head]
        self.head = (self.head + 1) % self.cap
        self.count -= 1
        return x
cq = CircularQueue(3)
print([cq.enqueue(i) for i in range(4)])
print(cq.dequeue(), cq.enqueue(9))
