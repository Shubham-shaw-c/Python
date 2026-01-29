nums = [5, 2, 8, 3, 6, 7, 4]
print(sorted(nums, key=lambda n: (n % 2, n)))
