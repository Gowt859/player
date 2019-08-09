n1 = int(input())
s1 = input()
vow = 'aeiouAEIOU'
s2 = ''
for i in s1 :
    if i not in vow : s2 = s2 + i
print(s2[::-1])
