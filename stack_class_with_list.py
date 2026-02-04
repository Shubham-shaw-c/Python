class Stack:
    def __init__(self):
        self.items = []
    def push(self, x):
        self.items.append(x)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def is_empty(self):
        return not self.items
s = Stack()
for i in (1, 2, 3):
    s.push(i)
print(s.pop(), s.peek(), s.is_empty())
