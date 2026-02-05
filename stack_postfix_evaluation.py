expr = "5 1 2 + 4 * + 3 -"
st = []
for tok in expr.split():
    if tok.isdigit():
        st.append(int(tok))
    else:
        b, a = st.pop(), st.pop()
        st.append({"+": a + b, "-": a - b, "*": a * b, "/": a / b}[tok])
print(st[0])
