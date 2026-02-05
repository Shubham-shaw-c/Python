def prec(c):
    return {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}.get(c, 0)
expr = "a+b*(c^d-e)^(f+g*h)-i"
out, st = [], []
for ch in expr:
    if ch.isalnum():
        out.append(ch)
    elif ch == "(":
        st.append(ch)
    elif ch == ")":
        while st[-1] != "(":
            out.append(st.pop())
        st.pop()
    else:
        while st and prec(st[-1]) >= prec(ch) and ch != "^":
            out.append(st.pop())
        st.append(ch)
while st:
    out.append(st.pop())
print("".join(out))
