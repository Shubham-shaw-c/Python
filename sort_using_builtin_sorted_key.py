people = [("Ana", 31), ("Bob", 25), ("Cid", 31), ("Dee", 22)]
print(sorted(people, key=lambda p: (-p[1], p[0])))
