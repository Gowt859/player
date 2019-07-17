g1,g2=map(int,input().split())
for j in range(g1,g2+1):
    if j>1:
        for n in range(2,j):
            if(j%n==0):
                break
        else:
            count=count+1
print(count)
