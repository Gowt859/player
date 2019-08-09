def freq1(s1) :
    dic1 = {}
    for c1 in s1 :
        if c1 in dic1 :
            dic1[c1] += 1
        else :
            dic1[c1] = 1
    return dic1

k1 = 0
s = 'kabali'
dic1 = freq1(s)
n = int(input())
for i in range(n) :
    s2 = input()
    dic2 = freq1(s2)
    if dic1 == dic2 : k1 += 1
print(k1)
