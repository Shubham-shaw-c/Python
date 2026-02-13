from collections import deque
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
dq = deque()
out = []
for i, n in enumerate(nums):
    while dq and nums[dq[-1]] <= n:
        dq.pop()
    dq.append(i)
    if dq[0] <= i - k:
        dq.popleft()
    if i >= k - 1:
        out.append(nums[dq[0]])
print(out)
