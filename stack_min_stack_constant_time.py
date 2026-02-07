class MinStack:
    def __init__(self):
        self.data = []
        self.mins = []
    def push(self, x):
        self.data.append(x)
        self.mins.append(min(x, self.mins[-1]) if self.mins else x)
    def pop(self):
        self.mins.pop()
        return self.data.pop()
    def minimum(self):
        return self.mins[-1]
m = MinStack()
for x in (5, 3, 7, 2):
    m.push(x)
print(m.minimum())
m.pop()
print(m.minimum())
