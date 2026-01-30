from collections import Counter
nums = [4, 6, 2, 6, 4, 4, 6, 1]
freq = Counter(nums)
print(sorted(nums, key=lambda n: (-freq[n], n)))
