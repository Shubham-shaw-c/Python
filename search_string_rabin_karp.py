text = "GEEKS FOR GEEKS"
pat = "GEEK"
base, mod = 256, 101
m = len(pat)
hp = ht = 0
for i in range(m):
    hp = (hp * base + ord(pat[i])) % mod
    ht = (ht * base + ord(text[i])) % mod
h = pow(base, m - 1, mod)
for i in range(len(text) - m + 1):
    if hp == ht and text[i:i + m] == pat:
        print("Found at", i)
    if i < len(text) - m:
        ht = ((ht - ord(text[i]) * h) * base + ord(text[i + m])) % mod
