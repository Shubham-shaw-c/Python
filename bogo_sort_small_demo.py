import random
random.seed(3)
data = [3, 1, 2]
tries = 0
while data != sorted(data):
    random.shuffle(data)
    tries += 1
print(data, tries > 0)
