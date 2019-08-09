n1,k1 = map(int,input().split())
k1 = k1%n1
L1 = list(map(int,input().split()))
L2 = L1[-k1:] + L1[:-k1]
print(*L2)
