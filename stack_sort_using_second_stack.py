data = [34, 3, 31, 98, 92, 23]
stack = []
for x in data:
    temp = []
    while stack and stack[-1] > x:
        temp.append(stack.pop())
    stack.append(x)
    while temp:
        stack.append(temp.pop())
print(stack)
