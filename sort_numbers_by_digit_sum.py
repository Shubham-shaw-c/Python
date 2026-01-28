nums = [56, 13, 99, 40, 101, 8]
print(sorted(nums, key=lambda n: sum(map(int, str(n)))))
