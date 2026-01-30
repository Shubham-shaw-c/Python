nums = [3, 30, 34, 5, 9]
from functools import cmp_to_key
nums_str = sorted(map(str, nums), key=cmp_to_key(lambda a, b: -1 if a + b > b + a else 1))
print("".join(nums_str))
