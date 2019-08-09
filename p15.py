s1 = input()
dic1 = {}
for i in s1 :
    if i in dic1 :
        dic1[i] += 1
    else :
        dic1[i] = 1
f1 = 0
for j in dic1 :
    if dic1[j] > f1 :
        f = dic1[j]
        key = j
print(key)
