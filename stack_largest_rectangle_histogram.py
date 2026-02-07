h = [2, 1, 5, 6, 2, 3]
st = []
best = 0
for i, x in enumerate(h + [0]):
    start = i
    while st and st[-1][1] > x:
        idx, height = st.pop()
        best = max(best, height * (i - idx))
        start = idx
    st.append((start, x))
print(best)
