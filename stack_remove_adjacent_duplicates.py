text = "abbaca"
st = []
for ch in text:
    if st and st[-1] == ch:
        st.pop()
    else:
        st.append(ch)
print("".join(st))
