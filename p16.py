n1 = int(input())
L1 = list(map(int,input().split()))
for j in L1 :
    if L1.count(j) == 1 :
        print(j)
        break
