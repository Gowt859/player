n1 = int(input())
m = n1
L = []
for i in range( 2,m) :
    if n1%i == 0 : L.append(i)
    while n1%i == 0 : n1 //= i
if len(L) == 0 : print(m)
else :           print(*L)
