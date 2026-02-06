nums = [4, 5, 2, 25, 7, 8]
result = [-1] * len(nums)
st = []
for i, n in enumerate(nums):
    while st and nums[st[-1]] < n:
        result[st.pop()] = n
    st.append(i)
print(result)
