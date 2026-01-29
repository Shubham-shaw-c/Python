order = {"red": 0, "green": 1, "blue": 2}
items = ["blue", "red", "green", "red", "blue"]
print(sorted(items, key=order.get))
