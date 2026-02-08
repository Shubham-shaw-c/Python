text = "datastructure"
stack = list(text)
print("".join(stack.pop() for _ in range(len(stack))))
