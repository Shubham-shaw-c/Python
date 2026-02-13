from collections import deque
people = deque(range(1, 8))
k = 3
while len(people) > 1:
    people.rotate(-(k - 1))
    print("Eliminated", people.popleft())
print("Survivor", people[0])
