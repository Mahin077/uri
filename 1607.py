s1 = "a"
s2 = "a"
v = ord(s2) - ord(s1)
if v<0:
    v = v + 26
print(v)