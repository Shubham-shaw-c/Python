words = ["pear", "fig", "apple", "kiwi", "date", "plum"]
print(sorted(words, key=lambda w: (len(w), w)))
