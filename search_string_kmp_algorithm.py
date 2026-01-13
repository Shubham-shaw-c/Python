def lps_table(p):
    lps = [0] * len(p)
    length = 0
    for i in range(1, len(p)):
        while length and p[i] != p[length]:
            length = lps[length - 1]
        if p[i] == p[length]:
            length += 1
        lps[i] = length
    return lps
def kmp(text, p):
    lps = lps_table(p)
    j = 0
    for i, ch in enumerate(text):
        while j and ch != p[j]:
            j = lps[j - 1]
        if ch == p[j]:
            j += 1
        if j == len(p):
            print("Match at", i - j + 1)
            j = lps[j - 1]
kmp("abxabcabcabyabcaby", "abcaby")
