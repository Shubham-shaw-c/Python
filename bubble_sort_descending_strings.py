words = ["pear", "apple", "fig", "banana", "kiwi"]
for i in range(len(words)):
    for j in range(len(words) - 1 - i):
        if words[j] < words[j + 1]:
            words[j], words[j + 1] = words[j + 1], words[j]
print(words)
