temps = [73, 74, 75, 71, 69, 72, 76, 73]
ans = [0] * len(temps)
st = []
for i, t in enumerate(temps):
    while st and temps[st[-1]] < t:
        j = st.pop()
        ans[j] = i - j
    st.append(i)
print(ans)
