s1 = input()
L1 = []
for c in s1 :
    k = ord(c) + 3
    if k > ord('Z') : k -= 26
    L1.append(chr(k))
s2 = ''.join(L1)
print(s2)
